> ## Documentation Index
> Fetch the complete documentation index at: https://developers.pandascore.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a rune

Get a single rune by ID
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
      "LoLRune": {
        "content": {
          "application/json": {
            "examples": {
              "/lol/runes/308": {
                "description": "/lol/runes/308",
                "value": {
                  "id": 308,
                  "name": "Lesser Quintessence of Precision"
                }
              }
            },
            "schema": {
              "$ref": "#/components/schemas/LoLRune"
            }
          }
        },
        "description": "A League-of-Legends rune"
      }
    },
    "schemas": {
      "LoLRune": {
        "additionalProperties": false,
        "deprecated": false,
        "properties": {
          "id": {
            "minimum": 1,
            "title": "LoLRuneID",
            "type": "integer"
          },
          "name": {
            "title": "LoLRuneName",
            "type": "string"
          }
        },
        "required": [
          "id",
          "name"
        ],
        "title": "LoLRune",
        "type": "object"
      },
      "LoLRuneID": {
        "minimum": 1,
        "title": "LoLRuneID",
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
    "/lol/runes/{lol_rune_id}": {
      "get": {
        "deprecated": true,
        "description": "Get a single rune by ID\n> ℹ️  \n> \n> This endpoint is available to all customers",
        "operationId": "get_lol_runes_lolRuneId",
        "parameters": [
          {
            "description": "A rune ID",
            "in": "path",
            "name": "lol_rune_id",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/LoLRuneID"
            }
          }
        ],
        "responses": {
          "200": {
            "$ref": "#/components/responses/LoLRune"
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
        "summary": "Get a rune",
        "tags": [
          "LoL runes"
        ],
        "x-readme": {
          "code-samples": [
            {
              "code": "curl --request GET \\\n     --url 'https://api.pandascore.co/lol/runes/{lol_rune_id}' \\\n     --header 'accept: application/json'\n",
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