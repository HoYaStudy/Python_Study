###############################################################################
# @brief    Python3 - JSON module.
# @version  v1.0
# @author   llChameleoNll <hoya128@gmail.com>
# @note
#   2017.08.18 - Created.
###############################################################################

'''
'''

import json

if __name__ == '__main__':
    testJSON = {
        "Item1": {
            "SubItem1": "value11",
            "SubItem2": {
                "Title1": "value121",
                "Title2": "value122"
            }
        },
        "Item2": {
            "SubItem1": "value21",
            "SubItem2": {
                "Title3": "value223",
                "Title4": "value224"
            }
        }
    }

    jsonItem1 = json.dumps(testJSON)
    print(jsonItem1)

    jsonItem2 = json.loads(jsonItem1)
    print(jsonItem2)
