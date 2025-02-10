#################################################################################
#  Licensed to the FIWARE Foundation (FF) under one                             #
#  or more contributor license agreements. The FF licenses this file            #
#  to you under the Apache License, Version 2.0 (the "License")                 #
#  you may not use this file except in compliance with the License.             #
#  You may obtain a copy of the License at                                      #
#                                                                               #
#      http://www.apache.org/licenses/LICENSE-2.0                               #
#                                                                               #
#  Unless required by applicable law or agreed to in writing, software          #
#  distributed under the License is distributed on an "AS IS" BASIS,            #
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.     #
#  See the License for the specific language governing permissions and          #
#  limitations under the License.                                               #
#  Author: Alberto Abella                                                       #
#################################################################################
import os

def test_file_exists(repo_path):
    """
    Test if a file exists.

    Parameters:
        repo_path (str): The path to the repository to check.

    Returns:
        tuple: (test_name: str, success: bool, message: list)
    """

    test_name = "Checking if the mandatory files according to the contribution manual are present"

    mandatory_files = [
        "schema.json",
        "examples/example.json",
        "examples/example-normalized.json",
        "examples/example.jsonld",
        "examples/example-normalized.jsonld",
        "notes.yaml",
        "ADOPTERS.yaml"
    ]
    output = []
    success = True

    for file in mandatory_files:
        path_to_file = os.path.join(repo_path, file)
        exist_file = os.path.exists(path_to_file)
        success = success and exist_file

        # Extract the file name from the path
        file_name = os.path.basename(file)

        if exist_file:
            output.append(f"The file {file_name} exists")
        else:
            output.append(f"*** The file {file_name} DOES NOT exist")

    return test_name, success, output