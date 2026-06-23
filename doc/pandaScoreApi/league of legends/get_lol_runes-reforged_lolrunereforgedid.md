> ## Documentation Index
> Fetch the complete documentation index at: https://developers.pandascore.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a LoL rune

Retrieve the latest version of a League of Legends (reforged) rune by its ID
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
      "LoLRuneReforged": {
        "content": {
          "application/json": {
            "examples": {
              "/lol/runes-reforged/53": {
                "description": "/lol/runes-reforged/53",
                "value": {
                  "id": 53,
                  "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/b8282c680e5d022dc564c54937a20a26.png",
                  "name": "Arcane Comet",
                  "type": "keystone"
                }
              }
            },
            "schema": {
              "$ref": "#/components/schemas/LoLRuneReforged"
            }
          }
        },
        "description": "A League-of-Legends (reforged) rune"
      }
    },
    "schemas": {
      "LoLRuneReforged": {
        "additionalProperties": false,
        "deprecated": false,
        "properties": {
          "id": {
            "description": "ID of the rune",
            "minimum": 1,
            "title": "LoLRuneReforgedID",
            "type": "integer"
          },
          "image_url": {
            "description": "URL to an image of the rune",
            "format": "uri",
            "title": "LoLRuneReforgedImageURL",
            "type": "string"
          },
          "name": {
            "description": "Name of the rune path",
            "title": "LoLRuneReforgedName",
            "type": "string"
          },
          "type": {
            "enum": [
              "keystone",
              "path",
              "shard",
              "slot1",
              "slot2",
              "slot3"
            ],
            "title": "LoLRuneReforgedType",
            "type": "string"
          }
        },
        "required": [
          "id",
          "image_url",
          "name",
          "type"
        ],
        "title": "LoLRuneReforged",
        "type": "object"
      },
      "LoLRuneReforgedID": {
        "description": "ID of the rune",
        "minimum": 1,
        "title": "LoLRuneReforgedID",
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
    "/lol/runes-reforged/{lol_rune_reforged_id}": {
      "get": {
        "description": "Retrieve the latest version of a League of Legends (reforged) rune by its ID\n> ℹ️  \n> \n> This endpoint is available to all customers",
        "operationId": "get_lol_runes-reforged_lolRuneReforgedId",
        "parameters": [
          {
            "description": "ID of the LoL rune",
            "in": "path",
            "name": "lol_rune_reforged_id",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/LoLRuneReforgedID"
            }
          }
        ],
        "responses": {
          "200": {
            "$ref": "#/components/responses/LoLRuneReforged"
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
        "summary": "Get a LoL rune",
        "tags": [
          "LoL runes"
        ],
        "x-readme": {
          "code-samples": [
            {
              "code": "curl --request GET \\\n     --url 'https://api.pandascore.co/lol/runes-reforged/{lol_rune_reforged_id}' \\\n     --header 'accept: application/json'\n",
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