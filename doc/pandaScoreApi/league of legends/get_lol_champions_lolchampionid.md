> ## Documentation Index
> Fetch the complete documentation index at: https://developers.pandascore.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a champion

Get a single champion by ID or by slug
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
      "LoLChampion": {
        "content": {
          "application/json": {
            "examples": {
              "/lol/champions/2527": {
                "description": "/lol/champions/2527",
                "value": {
                  "armor": 28,
                  "armorperlevel": 3.5,
                  "attackdamage": 60,
                  "attackdamageperlevel": 2.88,
                  "attackrange": 650,
                  "attackspeedoffset": null,
                  "attackspeedperlevel": 4,
                  "big_image_url": "https://cdn.pandascore.co/images/lol/champion/big_image/cdedf2069d61b212f4f70865102ab60d.jpg",
                  "crit": 0,
                  "critperlevel": 0,
                  "hp": 481,
                  "hpperlevel": 91,
                  "hpregen": 3.5,
                  "hpregenperlevel": 0.55,
                  "id": 2527,
                  "image_url": "https://cdn.pandascore.co/images/lol/champion/image/9c878f64e87d8271fc8c9d907b5db714.png",
                  "movespeed": 325,
                  "mp": 313.7,
                  "mpperlevel": 35,
                  "mpregen": 7.4,
                  "mpregenperlevel": 0.55,
                  "name": "Caitlyn",
                  "slug": "Caitlyn",
                  "spellblock": 30,
                  "spellblockperlevel": 0.5,
                  "videogame_versions": [
                    "9.17.1",
                    "9.16.1",
                    "9.15.1",
                    "9.14.1",
                    "9.13.1",
                    "9.12.1"
                  ]
                }
              }
            },
            "schema": {
              "$ref": "#/components/schemas/LoLChampion"
            }
          }
        },
        "description": "A League-of-Legends champion"
      }
    },
    "schemas": {
      "LoLChampion": {
        "additionalProperties": false,
        "deprecated": false,
        "properties": {
          "armor": {
            "minimum": 0,
            "title": "LoLArmor",
            "type": "number"
          },
          "armorperlevel": {
            "minimum": 0,
            "title": "LoLArmorPerLevel",
            "type": "number"
          },
          "attackdamage": {
            "minimum": 0,
            "title": "LoLAttackDamage",
            "type": "number"
          },
          "attackdamageperlevel": {
            "minimum": 0,
            "title": "LoLAttackDamagePerLevel",
            "type": "number"
          },
          "attackrange": {
            "minimum": 0,
            "title": "LoLAttackRange",
            "type": "number"
          },
          "attackspeedoffset": {
            "deprecated": false,
            "nullable": true,
            "title": "LoLAttackSpeedOffset",
            "type": "number"
          },
          "attackspeedperlevel": {
            "minimum": 0,
            "title": "LoLAttackSpeedPerLevel",
            "type": "number"
          },
          "big_image_url": {
            "format": "uri",
            "title": "LoLChampionBigImageURL",
            "type": "string"
          },
          "crit": {
            "minimum": 0,
            "title": "LoLCrit",
            "type": "number"
          },
          "critperlevel": {
            "minimum": 0,
            "title": "LoLCritPerLevel",
            "type": "number"
          },
          "hp": {
            "minimum": 0,
            "title": "LoLHP",
            "type": "number"
          },
          "hpperlevel": {
            "minimum": 0,
            "title": "LoLHPPerLevel",
            "type": "number"
          },
          "hpregen": {
            "minimum": 0,
            "title": "LoLHPRegen",
            "type": "number"
          },
          "hpregenperlevel": {
            "minimum": 0,
            "title": "LoLHPRegenPerLevel",
            "type": "number"
          },
          "id": {
            "minimum": 1,
            "title": "LoLChampionID",
            "type": "integer"
          },
          "image_url": {
            "format": "uri",
            "title": "LoLChampionImageURL",
            "type": "string"
          },
          "movespeed": {
            "minimum": 0,
            "title": "LoLMoveSpeed",
            "type": "number"
          },
          "mp": {
            "minimum": 0,
            "title": "LoLMP",
            "type": "number"
          },
          "mpperlevel": {
            "minimum": 0,
            "title": "LoLMPPerLevel",
            "type": "number"
          },
          "mpregen": {
            "minimum": 0,
            "title": "LoLMPRegen",
            "type": "number"
          },
          "mpregenperlevel": {
            "minimum": 0,
            "title": "LoLMPRegenPerLevel",
            "type": "number"
          },
          "name": {
            "title": "LoLChampionName",
            "type": "string"
          },
          "slug": {
            "description": "Human-readable identifier of the champion.",
            "title": "LoLChampionSlug",
            "type": "string"
          },
          "spellblock": {
            "minimum": 0,
            "title": "LoLMagicResist",
            "type": "number"
          },
          "spellblockperlevel": {
            "minimum": 0,
            "title": "LoLMagicResistPerLevel",
            "type": "number"
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
          "armor",
          "armorperlevel",
          "attackdamage",
          "attackdamageperlevel",
          "attackrange",
          "attackspeedoffset",
          "attackspeedperlevel",
          "big_image_url",
          "crit",
          "critperlevel",
          "hp",
          "hpperlevel",
          "hpregen",
          "hpregenperlevel",
          "id",
          "image_url",
          "movespeed",
          "mp",
          "mpperlevel",
          "mpregen",
          "mpregenperlevel",
          "name",
          "slug",
          "spellblock",
          "spellblockperlevel",
          "videogame_versions"
        ],
        "title": "LoLChampion",
        "type": "object"
      },
      "LoLChampionID": {
        "minimum": 1,
        "title": "LoLChampionID",
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
    "/lol/champions/{lol_champion_id}": {
      "get": {
        "description": "Get a single champion by ID or by slug\n> ℹ️  \n> \n> This endpoint is available to all customers",
        "operationId": "get_lol_champions_lolChampionId",
        "parameters": [
          {
            "description": "A champion ID",
            "in": "path",
            "name": "lol_champion_id",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/LoLChampionID"
            }
          }
        ],
        "responses": {
          "200": {
            "$ref": "#/components/responses/LoLChampion"
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
        "summary": "Get a champion",
        "tags": [
          "LoL champions"
        ],
        "x-readme": {
          "code-samples": [
            {
              "code": "curl --request GET \\\n     --url 'https://api.pandascore.co/lol/champions/{lol_champion_id}' \\\n     --header 'accept: application/json'\n",
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