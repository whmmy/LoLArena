> ## Documentation Index
> Fetch the complete documentation index at: https://developers.pandascore.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a LoL rune path

Retrieve the latest version of a League of Legends (reforged) rune path by its ID
> ℹ️  
> 
> This endpoint is available to all customers

# OpenAPI definition

```json
{
  "components": {
    "responses": {
      "Error400": {
        "content": {
          "application/json": {
            "schema": {
              "properties": {
                "error": {
                  "type": "string"
                }
              },
              "type": "object"
            }
          }
        },
        "description": "Bad request"
      },
      "Error401": {
        "content": {
          "application/json": {
            "schema": {
              "properties": {
                "error": {
                  "type": "string"
                }
              },
              "type": "object"
            }
          }
        },
        "description": "Unauthorized"
      },
      "Error403": {
        "content": {
          "application/json": {
            "schema": {
              "properties": {
                "error": {
                  "type": "string"
                }
              },
              "type": "object"
            }
          }
        },
        "description": "Forbidden"
      },
      "Error404": {
        "content": {
          "application/json": {
            "schema": {
              "properties": {
                "error": {
                  "type": "string"
                }
              },
              "type": "object"
            }
          }
        },
        "description": "Not found"
      },
      "Error422": {
        "content": {
          "application/json": {
            "schema": {
              "properties": {
                "error": {
                  "type": "string"
                }
              },
              "type": "object"
            }
          }
        },
        "description": "Unprocessable Entity"
      },
      "LoLRunePath": {
        "content": {
          "application/json": {
            "examples": {
              "/lol/runes-reforged-paths/1": {
                "description": "/lol/runes-reforged-paths/1",
                "value": {
                  "id": 1,
                  "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/346a8dc90cb18766f2dfde90672a6118.png",
                  "name": "Domination",
                  "runes": {
                    "keystones": [
                      4,
                      3,
                      2,
                      1
                    ],
                    "slot1": [
                      7,
                      6,
                      5
                    ],
                    "slot2": [
                      10,
                      9,
                      8
                    ],
                    "slot3": [
                      11,
                      14,
                      13,
                      12
                    ]
                  },
                  "videogame_versions": [
                    "14.10.1",
                    "14.9.1",
                    "14.8.1",
                    "14.7.1",
                    "14.6.1",
                    "14.5.1",
                    "14.4.1",
                    "14.3.1",
                    "14.2.1",
                    "14.1.1",
                    "13.24.1",
                    "13.23.1",
                    "13.22.1",
                    "13.21.1",
                    "13.19.1",
                    "13.18.1",
                    "13.17.1",
                    "13.16.1",
                    "13.15.1",
                    "13.14.1",
                    "13.13.1",
                    "13.12.1",
                    "13.11.1",
                    "13.10.1",
                    "13.9.1",
                    "13.8.1",
                    "13.7.1",
                    "13.6.1",
                    "13.5.1",
                    "13.4.1",
                    "13.3.1",
                    "13.1.1",
                    "12.23.1",
                    "12.22.1",
                    "12.21.1",
                    "12.20.1",
                    "12.19.1",
                    "12.18.1",
                    "12.17.1",
                    "12.16.1",
                    "12.15.1",
                    "12.14.1",
                    "12.13.1",
                    "12.12.1",
                    "12.11.1",
                    "12.10.1",
                    "12.9.1",
                    "12.8.1",
                    "12.7.1",
                    "12.6.1",
                    "12.5.1",
                    "12.4.1",
                    "12.3.1",
                    "12.2.1",
                    "12.1.1",
                    "11.24.1",
                    "11.23.1",
                    "11.22.1",
                    "11.21.1",
                    "11.20.1",
                    "11.19.1",
                    "11.18.1",
                    "11.17.1",
                    "11.16.1",
                    "11.15.1",
                    "11.14.1",
                    "11.13.1",
                    "11.12.1",
                    "11.11.1",
                    "11.10.1",
                    "11.9.1",
                    "11.8.1",
                    "11.7.1",
                    "11.6.1",
                    "11.5.1",
                    "11.4.1",
                    "11.3.1",
                    "11.2.1",
                    "11.1.1",
                    "10.25.1",
                    "10.24.1",
                    "10.23.1",
                    "10.22.1",
                    "10.21.1",
                    "10.20.1",
                    "10.19.1",
                    "10.10.3216176",
                    "10.10.3208608",
                    "9.9.1"
                  ]
                }
              }
            },
            "schema": {
              "$ref": "#/components/schemas/LoLRunePath"
            }
          }
        },
        "description": "A League-of-Legends runes path"
      }
    },
    "schemas": {
      "LoLRunePath": {
        "additionalProperties": false,
        "deprecated": false,
        "properties": {
          "id": {
            "description": "ID of the rune path",
            "minimum": 1,
            "title": "LoLRunePathID",
            "type": "integer"
          },
          "image_url": {
            "description": "URL to an image of the rune path",
            "format": "uri",
            "title": "LoLRunePathImageURL",
            "type": "string"
          },
          "name": {
            "description": "Name of the rune",
            "title": "LoLRunePathName",
            "type": "string"
          },
          "runes": {
            "additionalProperties": false,
            "deprecated": false,
            "properties": {
              "keystones": {
                "description": "IDs of the keystone runes available for this path",
                "items": {
                  "description": "ID of the rune",
                  "minimum": 1,
                  "title": "LoLRuneReforgedID",
                  "type": "integer"
                },
                "title": "LoLKeystoneRunes",
                "type": "array"
              },
              "slot1": {
                "description": "IDs of the slot 1 runes available for this path",
                "items": {
                  "description": "ID of the rune",
                  "minimum": 1,
                  "title": "LoLRuneReforgedID",
                  "type": "integer"
                },
                "maxItems": 4,
                "minItems": 3,
                "title": "LoLSlot1Runes",
                "type": "array"
              },
              "slot2": {
                "description": "IDs of the slot 2 runes available for this path",
                "items": {
                  "description": "ID of the rune",
                  "minimum": 1,
                  "title": "LoLRuneReforgedID",
                  "type": "integer"
                },
                "maxItems": 6,
                "minItems": 3,
                "title": "LoLSlot2Runes",
                "type": "array"
              },
              "slot3": {
                "description": "IDs of the slot 3 runes available for this path",
                "items": {
                  "description": "ID of the rune",
                  "minimum": 1,
                  "title": "LoLRuneReforgedID",
                  "type": "integer"
                },
                "maxItems": 4,
                "minItems": 3,
                "title": "LoLSlot3Runes",
                "type": "array"
              }
            },
            "required": [
              "keystones",
              "slot1",
              "slot2",
              "slot3"
            ],
            "title": "LoLRunePathRunesObject",
            "type": "object"
          },
          "videogame_versions": {
            "description": "Array of of video game versions (ie. patches) for this resource",
            "items": {
              "pattern": "^[0-9]+\\.[0-9]+(\\.[0-9]+)?$",
              "title": "VideogameVersion",
              "type": "string"
            },
            "title": "VideogameVersions",
            "type": "array"
          }
        },
        "required": [
          "id",
          "image_url",
          "name",
          "runes",
          "videogame_versions"
        ],
        "title": "LoLRunePath",
        "type": "object"
      },
      "LoLRunePathID": {
        "description": "ID of the rune path",
        "minimum": 1,
        "title": "LoLRunePathID",
        "type": "integer"
      }
    },
    "securitySchemes": {
      "BearerToken": {
        "scheme": "bearer",
        "type": "http"
      },
      "QueryToken": {
        "in": "query",
        "name": "token",
        "type": "apiKey"
      }
    }
  },
  "info": {
    "title": "League of Legends",
    "version": "2.62.8"
  },
  "openapi": "3.0.0",
  "paths": {
    "/lol/runes-reforged-paths/{lol_rune_path_id}": {
      "get": {
        "description": "Retrieve the latest version of a League of Legends (reforged) rune path by its ID\n> ℹ️  \n> \n> This endpoint is available to all customers",
        "operationId": "get_lol_runes-reforged-paths_lolRunePathId",
        "parameters": [
          {
            "description": "ID of the LoL rune path",
            "in": "path",
            "name": "lol_rune_path_id",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/LoLRunePathID"
            }
          }
        ],
        "responses": {
          "200": {
            "$ref": "#/components/responses/LoLRunePath"
          },
          "400": {
            "$ref": "#/components/responses/Error400"
          },
          "401": {
            "$ref": "#/components/responses/Error401"
          },
          "403": {
            "$ref": "#/components/responses/Error403"
          },
          "404": {
            "$ref": "#/components/responses/Error404"
          },
          "422": {
            "$ref": "#/components/responses/Error422"
          }
        },
        "summary": "Get a LoL rune path",
        "tags": [
          "LoL runes"
        ],
        "x-readme": {
          "code-samples": [
            {
              "code": "curl --request GET \\\n     --url 'https://api.pandascore.co/lol/runes-reforged-paths/{lol_rune_path_id}' \\\n     --header 'accept: application/json'\n",
              "language": "curl"
            }
          ]
        }
      }
    }
  },
  "security": [
    {
      "BearerToken": []
    },
    {
      "QueryToken": []
    }
  ],
  "servers": [
    {
      "url": "https://api.pandascore.co/",
      "variables": {}
    }
  ],
  "x-readme": {
    "explorer-enabled": false,
    "samples-languages": [
      "curl"
    ]
  }
}
```