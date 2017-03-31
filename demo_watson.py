from watson_developer_cloud import NaturalLanguageClassifierV1

natural_language_classifier = NaturalLanguageClassifierV1(
  username='',
  password='')


# import json
# from watson_developer_cloud import NaturalLanguageClassifierV1


# with open('dataset.csv', 'rb') as training_data:
#   classifier = natural_language_classifier.create(
#     training_data=training_data,
#     name='Official Resarch Paper Class',
#     language='en'
#   )
# print(json.dumps(classifier, indent=2))


import json
from watson_developer_cloud import NaturalLanguageClassifierV1 as NaturalLanguageClassifier


classifiers = natural_language_classifier.list()
print(json.dumps(classifiers, indent=2))


status = natural_language_classifier.status('')
print (json.dumps(status, indent=2))
status = natural_language_classifier.status('')
print (json.dumps(status, indent=2))

from watson_developer_cloud import NaturalLanguageClassifierV1


classes = natural_language_classifier.classify('', 'enchanted scissors: a scissor interface for support in cutting and interactive fabrication.')
print(json.dumps(classes, indent=2))




# ---- END OF THE CODE ----