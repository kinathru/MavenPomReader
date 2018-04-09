from xml.etree import ElementTree as et

ns = "http://maven.apache.org/POM/4.0.0"
et.register_namespace('', ns)
tree = et.ElementTree()
tree.parse('pom.xml')
root = tree.getroot()

p = root.find("{%s}profiles" % ns)

for profile in p.findall("{%s}profile" % ns):
    profileId = profile.find("{%s}id" % ns)
    print(profileId.text)

print('done')
