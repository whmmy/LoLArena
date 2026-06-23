> ## Documentation Index
> Fetch the complete documentation index at: https://developers.pandascore.co/llms.txt
> Use this file to discover all available pages before exploring further.

# List champions

List champions
> ℹ️  
> 
> This endpoint is available to all customers

# OpenAPI definition

```json
{
  "components": {
    "parameters": {
      "Page": {
        "description": "Pagination in the form of `page=2` or `page[size]=30&page[number]=2`",
        "in": "query",
        "name": "page",
        "required": false,
        "schema": {
          "oneOf": [
            {
              "default": 1,
              "minimum": 1,
              "type": "integer"
            },
            {
              "additionalProperties": false,
              "properties": {
                "number": {
                  "default": 1,
                  "minimum": 1,
                  "type": "integer"
                },
                "size": {
                  "default": 50,
                  "maximum": 100,
                  "minimum": 1,
                  "type": "integer"
                }
              },
              "type": "object"
            }
          ]
        }
      },
      "PerPage": {
        "description": "Equivalent to `page[size]`",
        "example": 5,
        "in": "query",
        "name": "per_page",
        "required": false,
        "schema": {
          "default": 50,
          "maximum": 100,
          "minimum": 1,
          "type": "integer"
        }
      }
    },
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
      "LoLChampions": {
        "content": {
          "application/json": {
            "examples": {
              "/lol/champions?page[size]=1": {
                "description": "/lol/champions?page[size]=1",
                "value": [
                  {
                    "armor": 35,
                    "armorperlevel": 5,
                    "attackdamage": 63,
                    "attackdamageperlevel": 3,
                    "attackrange": 175,
                    "attackspeedoffset": null,
                    "attackspeedperlevel": 3.5,
                    "big_image_url": "https://cdn.pandascore.co/images/lol/champion/big_image/0024c94f-e726-4b1a-ae9b-c54a3b903175.jpg",
                    "crit": 0,
                    "critperlevel": 0,
                    "hp": 640,
                    "hpperlevel": 106,
                    "hpregen": 8,
                    "hpregenperlevel": 0.7,
                    "id": 3513,
                    "image_url": "https://cdn.pandascore.co/images/lol/champion/image/7528230f-14f2-4687-9e1b-a6dc8053848e.png",
                    "movespeed": 345,
                    "mp": 274,
                    "mpperlevel": 55,
                    "mpregen": 7.25,
                    "mpregenperlevel": 0.45,
                    "name": "Xin Zhao",
                    "slug": "XinZhao",
                    "spellblock": 32,
                    "spellblockperlevel": 2.05,
                    "videogame_versions": [
                      "14.18.1"
                    ]
                  }
                ]
              }
            },
            "schema": {
              "$ref": "#/components/schemas/LoLChampions"
            }
          }
        },
        "description": "A list of League-of-Legends champions"
      }
    },
    "schemas": {
      "LoLChampions": {
        "items": {
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
        "title": "LoLChampions",
        "type": "array"
      },
      "filter_over_LoLChampions": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "armor": {
            "items": {
              "minimum": 0,
              "title": "LoLArmor",
              "type": "number"
            },
            "minItems": 1,
            "type": "array"
          },
          "armorperlevel": {
            "items": {
              "minimum": 0,
              "title": "LoLArmorPerLevel",
              "type": "number"
            },
            "minItems": 1,
            "type": "array"
          },
          "attackdamage": {
            "items": {
              "minimum": 0,
              "title": "LoLAttackDamage",
              "type": "number"
            },
            "minItems": 1,
            "type": "array"
          },
          "attackdamageperlevel": {
            "items": {
              "minimum": 0,
              "title": "LoLAttackDamagePerLevel",
              "type": "number"
            },
            "minItems": 1,
            "type": "array"
          },
          "attackrange": {
            "items": {
              "minimum": 0,
              "title": "LoLAttackRange",
              "type": "number"
            },
            "minItems": 1,
            "type": "array"
          },
          "attackspeedoffset": {
            "items": {
              "title": "LoLAttackSpeedOffset",
              "type": "number"
            },
            "minItems": 1,
            "type": "array"
          },
          "attackspeedperlevel": {
            "items": {
              "minimum": 0,
              "title": "LoLAttackSpeedPerLevel",
              "type": "number"
            },
            "minItems": 1,
            "type": "array"
          },
          "crit": {
            "items": {
              "minimum": 0,
              "title": "LoLCrit",
              "type": "number"
            },
            "minItems": 1,
            "type": "array"
          },
          "critperlevel": {
            "items": {
              "minimum": 0,
              "title": "LoLCritPerLevel",
              "type": "number"
            },
            "minItems": 1,
            "type": "array"
          },
          "hp": {
            "items": {
              "minimum": 0,
              "title": "LoLHP",
              "type": "number"
            },
            "minItems": 1,
            "type": "array"
          },
          "hpperlevel": {
            "items": {
              "minimum": 0,
              "title": "LoLHPPerLevel",
              "type": "number"
            },
            "minItems": 1,
            "type": "array"
          },
          "hpregen": {
            "items": {
              "minimum": 0,
              "title": "LoLHPRegen",
              "type": "number"
            },
            "minItems": 1,
            "type": "array"
          },
          "hpregenperlevel": {
            "items": {
              "minimum": 0,
              "title": "LoLHPRegenPerLevel",
              "type": "number"
            },
            "minItems": 1,
            "type": "array"
          },
          "id": {
            "items": {
              "minimum": 1,
              "title": "LoLChampionID",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "movespeed": {
            "items": {
              "minimum": 0,
              "title": "LoLMoveSpeed",
              "type": "number"
            },
            "minItems": 1,
            "type": "array"
          },
          "mp": {
            "items": {
              "minimum": 0,
              "title": "LoLMP",
              "type": "number"
            },
            "minItems": 1,
            "type": "array"
          },
          "mpperlevel": {
            "items": {
              "minimum": 0,
              "title": "LoLMPPerLevel",
              "type": "number"
            },
            "minItems": 1,
            "type": "array"
          },
          "mpregen": {
            "items": {
              "minimum": 0,
              "title": "LoLMPRegen",
              "type": "number"
            },
            "minItems": 1,
            "type": "array"
          },
          "mpregenperlevel": {
            "items": {
              "minimum": 0,
              "title": "LoLMPRegenPerLevel",
              "type": "number"
            },
            "minItems": 1,
            "type": "array"
          },
          "name": {
            "items": {
              "title": "LoLChampionName",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "slug": {
            "items": {
              "description": "Human-readable identifier of the champion.",
              "title": "LoLChampionSlug",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "spellblock": {
            "items": {
              "minimum": 0,
              "title": "LoLMagicResist",
              "type": "number"
            },
            "minItems": 1,
            "type": "array"
          },
          "spellblockperlevel": {
            "items": {
              "minimum": 0,
              "title": "LoLMagicResistPerLevel",
              "type": "number"
            },
            "minItems": 1,
            "type": "array"
          },
          "videogame_version": {
            "description": "Filter by the names of videogame versions, all versions using `filter[videogame_version]=all`, or by the latest version using `filter[videogame_version]=latest`"
          }
        },
        "type": "object"
      },
      "range_over_LoLChampions": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "armor": {
            "items": {
              "minimum": 0,
              "title": "LoLArmor",
              "type": "number"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "armorperlevel": {
            "items": {
              "minimum": 0,
              "title": "LoLArmorPerLevel",
              "type": "number"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "attackdamage": {
            "items": {
              "minimum": 0,
              "title": "LoLAttackDamage",
              "type": "number"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "attackdamageperlevel": {
            "items": {
              "minimum": 0,
              "title": "LoLAttackDamagePerLevel",
              "type": "number"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "attackrange": {
            "items": {
              "minimum": 0,
              "title": "LoLAttackRange",
              "type": "number"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "attackspeedoffset": {
            "items": {
              "title": "LoLAttackSpeedOffset",
              "type": "number"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "attackspeedperlevel": {
            "items": {
              "minimum": 0,
              "title": "LoLAttackSpeedPerLevel",
              "type": "number"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "crit": {
            "items": {
              "minimum": 0,
              "title": "LoLCrit",
              "type": "number"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "critperlevel": {
            "items": {
              "minimum": 0,
              "title": "LoLCritPerLevel",
              "type": "number"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "hp": {
            "items": {
              "minimum": 0,
              "title": "LoLHP",
              "type": "number"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "hpperlevel": {
            "items": {
              "minimum": 0,
              "title": "LoLHPPerLevel",
              "type": "number"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "hpregen": {
            "items": {
              "minimum": 0,
              "title": "LoLHPRegen",
              "type": "number"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "hpregenperlevel": {
            "items": {
              "minimum": 0,
              "title": "LoLHPRegenPerLevel",
              "type": "number"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "id": {
            "items": {
              "minimum": 1,
              "title": "LoLChampionID",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "movespeed": {
            "items": {
              "minimum": 0,
              "title": "LoLMoveSpeed",
              "type": "number"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "mp": {
            "items": {
              "minimum": 0,
              "title": "LoLMP",
              "type": "number"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "mpperlevel": {
            "items": {
              "minimum": 0,
              "title": "LoLMPPerLevel",
              "type": "number"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "mpregen": {
            "items": {
              "minimum": 0,
              "title": "LoLMPRegen",
              "type": "number"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "mpregenperlevel": {
            "items": {
              "minimum": 0,
              "title": "LoLMPRegenPerLevel",
              "type": "number"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "name": {
            "items": {
              "title": "LoLChampionName",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "spellblock": {
            "items": {
              "minimum": 0,
              "title": "LoLMagicResist",
              "type": "number"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "spellblockperlevel": {
            "items": {
              "minimum": 0,
              "title": "LoLMagicResistPerLevel",
              "type": "number"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          }
        },
        "type": "object"
      },
      "search_over_LoLChampions": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "name": {
            "title": "LoLChampionName",
            "type": "string"
          }
        },
        "type": "object"
      },
      "sort_over_LoLChampions": {
        "items": {
          "enum": [
            "armor",
            "-armor",
            "armorperlevel",
            "-armorperlevel",
            "attackdamage",
            "-attackdamage",
            "attackdamageperlevel",
            "-attackdamageperlevel",
            "attackrange",
            "-attackrange",
            "attackspeedoffset",
            "-attackspeedoffset",
            "attackspeedperlevel",
            "-attackspeedperlevel",
            "crit",
            "-crit",
            "critperlevel",
            "-critperlevel",
            "hp",
            "-hp",
            "hpperlevel",
            "-hpperlevel",
            "hpregen",
            "-hpregen",
            "hpregenperlevel",
            "-hpregenperlevel",
            "id",
            "-id",
            "movespeed",
            "-movespeed",
            "mp",
            "-mp",
            "mpperlevel",
            "-mpperlevel",
            "mpregen",
            "-mpregen",
            "mpregenperlevel",
            "-mpregenperlevel",
            "name",
            "-name",
            "spellblock",
            "-spellblock",
            "spellblockperlevel",
            "-spellblockperlevel"
          ]
        },
        "minItems": 1,
        "type": "array"
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
    "/lol/champions": {
      "get": {
        "description": "List champions\n> ℹ️  \n> \n> This endpoint is available to all customers",
        "operationId": "get_lol_champions",
        "parameters": [
          {
            "description": "Options to filter results. String fields are case sensitive\nFor more information on filtering, see [docs](/docs/filtering-and-sorting#filter).",
            "explode": true,
            "in": "query",
            "name": "filter",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/filter_over_LoLChampions"
            },
            "style": "deepObject"
          },
          {
            "description": "Options to select results within ranges\nFor more information on ranges, see [docs](/docs/filtering-and-sorting#range).",
            "explode": true,
            "in": "query",
            "name": "range",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/range_over_LoLChampions"
            },
            "style": "deepObject"
          },
          {
            "description": "Options to sort results\nFor more information on sorting, see [docs](/docs/filtering-and-sorting#sort).",
            "in": "query",
            "name": "sort",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/sort_over_LoLChampions"
            }
          },
          {
            "description": "Options to search results\nFor more information on searching, see [docs](/docs/filtering-and-sorting#search).",
            "explode": true,
            "in": "query",
            "name": "search",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/search_over_LoLChampions"
            },
            "style": "deepObject"
          },
          {
            "$ref": "#/components/parameters/Page"
          },
          {
            "$ref": "#/components/parameters/PerPage"
          }
        ],
        "responses": {
          "200": {
            "$ref": "#/components/responses/LoLChampions"
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
        "summary": "List champions",
        "tags": [
          "LoL champions"
        ],
        "x-readme": {
          "code-samples": [
            {
              "code": "curl --request GET \\\n     --url 'https://api.pandascore.co/lol/champions' \\\n     --header 'accept: application/json'\n",
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