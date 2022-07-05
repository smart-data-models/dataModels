################################################################################
#  Licensed to the FIWARE Foundation (FF) under one
#  or more contributor license agreements. The FF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
# limitations under the License.
################################################################################

# This program takes either a keyvalues payload and converts it into a normalized version and the other way round


def normalized2keyvalues(normalizedPayload):
    import json


    normalizedDict = json.loads(normalizedPayload)
    output = {}
    # print(normalizedDict)
    for element in normalizedDict:
        print(normalizedDict[element])
        try:
            value = normalizedDict[element]["value"]
            output[element] = value
        except:
            output[element] = normalizedDict[element]

    print(json.dumps(output, indent=4, sort_keys=True))
    return output


def keyvalues2normalized(keyvaluesPayload):
    import json

    def valid_date(datestring):
        import re
        date = datestring.split("T")[0]
        print(date)
        try:
            validDate = re.match('^[0-9]{2,4}[-/][0-9]{2}[-/][0-9]{2,4}$', date)
            print(validDate)
        except ValueError:
            return False

        if validDate is not None:
            return True
        else:
            return False

    keyvaluesDict = keyvaluesPayload
    output = {}
    # print(normalizedDict)
    for element in keyvaluesDict:
        item = {}
        print(keyvaluesDict[element])
        if isinstance(keyvaluesDict[element], list):
            # it is an array
            item["type"] = "array"
            item["value"] = keyvaluesDict[element]
        elif isinstance(keyvaluesDict[element], dict):
            # it is an object
            item["type"] = "object"
            item["value"] = keyvaluesDict[element]
        elif isinstance(keyvaluesDict[element], str):
            if valid_date(keyvaluesDict[element]):
                # it is a date
                item["format"] = "date-time"
            # it is a string
            item["type"] = "string"
            item["value"] = keyvaluesDict[element]
        elif keyvaluesDict[element] == True:
            # it is an boolean
            item["type"] = "boolean"
            item["value"] = "true"
        elif keyvaluesDict[element] == False:
            # it is an boolean
            item["type"] = "boolean"
            item["value"] = "false"
        elif isinstance(keyvaluesDict[element], int) or isinstance(keyvaluesDict[element], float):
            # it is an number
            item["type"] = "number"
            item["value"] = keyvaluesDict[element]
        else:
            print("*** other type ***")
            print("I do now know what is it")
            print(keyvaluesDict[element])
            print("--- other type ---")
        output[element] = item

    if "id" in output:
        output["id"] = output["id"]["value"]
    if "type" in output:
        output["type"] = output["type"]["value"]

    print(output)
    return output





keyvaluesPayload = {
	"id": "https://smart-data-models.github.io/IUDX/TransitManagement/schema.json",
	"type": "TransitManagement",
	"vehicleType":"hopper",
	"trip_delay":11968,
	"agency_lang":"en",
	"depot_name":"BHESTAN DEPOT",
	"travelTime":"22:11:14",
	"direction_id":0,
	"schedule_relationship":"SCHEDULED",
	"vehicle_id":"52TC12",
	"agency_fare_url":"http://charteredbike.in/surat/?page_id=1021",
	"actual_trip_end_time":"2021-10-28T08:24:22+05:30",
	"last_tracked_time":"08:13:22",
	"standing_capacity":20,
	"last_stop_arrival_time":"13:30:12",
	"agency_id":"agency001",
	"current_status":"INCOMING_AT",
	"route_type":"1",
	"speed":28,
	"route_id":"17AD",
	"seating_capacity":70,
	"vehicle_label":"A03",
	"timestamp":"2021-10-28T08:13:22+05:30",
	"arrival_time":"22:00:28",
	"route_long_name":"Baiyappanahalli to Mysuru Road",
	"agency_timezone":"Asia/Kolkata",
	"stop_code":"F12",
	"agency_name":"Chartered Bike Surat",
	"route_desc":"Phase1-Phase2",
	"license_plate":"GJ05BX1583",
	"stop_id":"1016",
	"uncertainity":0,
	"route_color":"00FFFF",
	"travelDistance":9.00174,
	"actual_trip_start_time":"2021-10-28T07:46:51+05:30",
	"bearing":90,
	"stop_sequence":24,
	"start_date":"2022-03-01",
	"current_stop_sequence":1001,
	"start_time":"11:15:35",
	"trip_id":"23952340",
	"route_text_color":"FFD700",
	"ac_available":"yes",
	"tripDirection":"DN",
	"agency_url": "http://charteredbike.in/surat/",
	"routeStopSequence":["10","1001","1002","1003","1004","1005"],
	"trip_direction":"DN",
	"departure_time":"22:00:33",
	"last_stop_id":"4032",
	"route_short_name":"Purple Line",
	"stop_name":"DEVASHISH NAGAR MORA BHAGAL",
	"depot_id":"1",
	"observationDateTime":"2021-10-28T08:13:22+05:30"
}




normalizedPayload = """
{
  "id": "urn:ngsi-ld:AirQualityForecast:France-AirQualityForecast-12345_2022-07-01T18:00:00_2022-07-01T00:00:00",
  "type": "AirQualityForecast",
  "address": {
    "type": "Property",
    "value": {
      "addressCountry": "France",
      "postalCode": "06200",
      "addressLocality": "Nice",
      "type": "PostalAddress"
    }
  },
  "location": {
    "type": "GeoProperty",
    "value": {
      "type": "Point",
      "coordinates": [
        7.2032497427380235,
        43.68056738083439
      ]
    }
  },
  "dataProvider": {
    "type": "Property",
    "value": "IMREDD_UCA_Nice"
  },
  "dateIssued": {
    "type": "Property",
    "value": {
      "@type": "DateTime",
      "@value": "2022-07-01T10:40:01.00Z"
    }
  },
  "dateRetrieved": {
    "type": "Property",
    "value": {
      "@type": "DateTime",
      "@value": "2022-07-01T12:57:24.00Z"
    }
  },
  "validFrom": {
    "type": "Property",
    "value": {
      "@type": "DateTime",
      "@value": "2022-07-01T17:00:00.00Z"
    }
  },
  "validTo": {
    "type": "Property",
    "value": {
      "@type": "DateTime",
      "@value": "2022-07-01T18:00:00.00Z"
    }
  },
  "validity": {
    "type": "Property",
    "value": "2022-07-01T17:00:00+01:00/2022-07-01T18:00:00+01:00"
  },
  "airQualityIndex": {
    "type": "Property",
    "value": 3
  },
  "airQualityLevel": {
    "type": "Property",
    "value": "moderate"
  },
  "co2": {
    "type": "Property",
    "value": 45,
    "unitCode": "GQ"
  },
  "no2": {
    "type": "Property",
    "value": 69,
    "unitCode": "GQ"
  },
  "o3": {
    "type": "Property",
    "value": 100,
    "unitCode": "GQ"
  },
  "nox": {
    "type": "Property",
    "value": 139,
    "unitCode": "GQ"
  },
  "so2": {
    "type": "Property",
    "value": 11,
    "unitCode": "GQ"
  },
  "pm10": {
    "type": "Property",
    "value": 19,
    "unitCode": "GQ"
  },
  "pm25": {
    "type": "Property",
    "value": 21,
    "unitCode": "GQ"
  },
  "temperature": {
    "type": "Property",
    "value": 12.2
  },
  "relativeHumidity": {
    "type": "Property",
    "value": 0.54
  },
  "windSpeed": {
    "type": "Property",
    "value": 0.64
  },
  "precipitation": {
    "type": "Property",
    "value": 0
  },
  "typeOfLocation": {
    "type": "Property",
    "value": "outdoor"
  },
  "@context": [
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Environment/master/context.jsonld"
  ]
}
"""

normalized2keyvalues(normalizedPayload)
# keyvalues2normalized(keyvaluesPayload)
