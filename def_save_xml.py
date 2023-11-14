import xml.etree.ElementTree as ET
from pyspark.sql.types import MapType, StringType, ArrayType,StructType, StructField, StringType, IntegerType
cols =  ['C' + str(i) for i in range(1, 222)]
columns = [ StructField("RECID", StringType(), True),
            StructField("M_SEQ", StringType(), True),  
            StructField("N_SEQ", StringType(), True)] + [
            StructField("C{}".format(i), StringType(), True) for i in range(1, 221 + 1)]

schema = StructType(columns)

def parse_xml(xml_string):
    root = ET.fromstring(xml_string.encode('utf-8'))
    id_value = root.attrib.get('id', None)
    data={}
    data[('1','1')] = {'RECID': id_value, 'M_SEQ': 1, 'N_SEQ': 1}
    data[('1','1')].update({key: "" for key in cols})
    for child in root:
        text_value = child.text if child.text is not None else ""
        m=child.attrib.get("m", "1")
        n=child.attrib.get("n", "1")
        if (m,n) == ('1','1'):
            data[(m, n)][child.tag.upper()]=text_value
    for child in root:
      text_value = child.text if child.text is not None else ""
      m=child.attrib.get("m", "1")
      n=child.attrib.get("n", "1")
      if (m, n) not in data:
        data[(m,n)] = {'RECID': id_value, 'M_SEQ': m, 'N_SEQ': n}
        data[(m,n)].update({key: data[('1','1')][key] for key in cols})
      if (m,n) != ('1','1'):
          data[(m,n)][child.tag.upper()]=text_value
    data = [[item[key] for key in ['RECID', 'M_SEQ', 'N_SEQ'] + cols] for item in data.values()]
    return data
def process_rdd(time, rdd):
    if not rdd.isEmpty():
        sqlctx = getSqlContextInstance(rdd.context)
        df1 = sqlctx.createDataFrame(rdd, schema)          
        rdd=df1.rdd
    return rdd
if FBN:
  FBN=FBN.map(lambda x: x.after[1]) 
  FBN=FBN.flatMap(parse_xml)
  TABLEFUNCTION=FBN.transform(process_rdd)