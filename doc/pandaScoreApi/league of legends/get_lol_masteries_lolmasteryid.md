> ## Documentation Index
> Fetch the complete documentation index at: https://developers.pandascore.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a mastery

Get a single mastery by ID
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
      "LoLMastery": {
        "content": {
          "application/json": {
            "examples": {
              "/lol/masteries/689": {
                "description": "/lol/masteries/689",
                "value": {
                  "id": 689,
                  "name": "Stoneborn Pact"
                }
              }
            },
            "schema": {
              "$ref": "#/components/schemas/LoLMastery"
            }
          }
        },
        "description": "A League-of-Legends mastery"
      }
    },
    "schemas": {
      "LoLMastery": {
        "additionalProperties": false,
        "deprecated": false,
        "properties": {
          "id": {
            "minimum": 1,
            "title": "LoLMasteryID",
            "type": "integer"
          },
          "name": {
            "title": "LoLMasteryName",
            "type": "string"
          }
        },
        "required": [
          "id",
          "name"
        ],
        "title": "LoLMastery",
        "type": "object"
      },
      "LoLMasteryID": {
        "minimum": 1,
        "title": "LoLMasteryID",
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
    "/lol/masteries/{lol_mastery_id}": {
      "get": {
        "description": "Get a single mastery by ID\n> ℹ️  \n> \n> This endpoint is available to all customers",
        "operationId": "get_lol_masteries_lolMasteryId",
        "parameters": [
          {
            "description": "A mastery ID",
            "in": "path",
            "name": "lol_mastery_id",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/LoLMasteryID"
            }
          }
        ],
        "responses": {
          "200": {
            "$ref": "#/components/responses/LoLMastery"
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
        "summary": "Get a mastery",
        "tags": [
          "LoL masteries"
        ],
        "x-readme": {
          "code-samples": [
            {
              "code": "curl --request GET \\\n     --url 'https://api.pandascore.co/lol/masteries/{lol_mastery_id}' \\\n     --header 'accept: application/json'\n",
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