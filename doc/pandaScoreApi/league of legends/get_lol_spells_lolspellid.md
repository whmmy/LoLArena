> ## Documentation Index
> Fetch the complete documentation index at: https://developers.pandascore.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a spell

Get a single spell by ID
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
      "LoLSpell": {
        "content": {
          "application/json": {
            "examples": {
              "/lol/spells/39": {
                "description": "/lol/spells/39",
                "value": {
                  "id": 39,
                  "image_url": "https://cdn.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                  "name": "Teleport"
                }
              }
            },
            "schema": {
              "$ref": "#/components/schemas/LoLSpell"
            }
          }
        },
        "description": "A League-of-Legends spell"
      }
    },
    "schemas": {
      "LoLSpell": {
        "additionalProperties": false,
        "deprecated": false,
        "properties": {
          "id": {
            "minimum": 1,
            "title": "LoLSpellID",
            "type": "integer"
          },
          "image_url": {
            "format": "uri",
            "title": "LoLSpellImageURL",
            "type": "string"
          },
          "name": {
            "title": "LoLSpellName",
            "type": "string"
          }
        },
        "required": [
          "id",
          "image_url",
          "name"
        ],
        "title": "LoLSpell",
        "type": "object"
      },
      "LoLSpellID": {
        "minimum": 1,
        "title": "LoLSpellID",
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
    "/lol/spells/{lol_spell_id}": {
      "get": {
        "description": "Get a single spell by ID\n> ℹ️  \n> \n> This endpoint is available to all customers",
        "operationId": "get_lol_spells_lolSpellId",
        "parameters": [
          {
            "description": "A spell ID",
            "in": "path",
            "name": "lol_spell_id",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/LoLSpellID"
            }
          }
        ],
        "responses": {
          "200": {
            "$ref": "#/components/responses/LoLSpell"
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
        "summary": "Get a spell",
        "tags": [
          "LoL spells"
        ],
        "x-readme": {
          "code-samples": [
            {
              "code": "curl --request GET \\\n     --url 'https://api.pandascore.co/lol/spells/{lol_spell_id}' \\\n     --header 'accept: application/json'\n",
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