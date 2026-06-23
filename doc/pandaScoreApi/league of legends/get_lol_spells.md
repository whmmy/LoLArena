> ## Documentation Index
> Fetch the complete documentation index at: https://developers.pandascore.co/llms.txt
> Use this file to discover all available pages before exploring further.

# List spells

List spells
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
      "LoLSpells": {
        "content": {
          "application/json": {
            "examples": {
              "/lol/spells?page[size]=1": {
                "description": "/lol/spells?page[size]=1",
                "value": [
                  {
                    "id": 122,
                    "image_url": "https://cdn.pandascore.co/images/lol/spell/image/3a9e0f3dd1b09b665189bcd378a639fa.png",
                    "name": "Placeholder and Attack-Smite"
                  }
                ]
              }
            },
            "schema": {
              "$ref": "#/components/schemas/LoLSpells"
            }
          }
        },
        "description": "A list of League-of-Legends spells"
      }
    },
    "schemas": {
      "LoLSpells": {
        "items": {
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
        "title": "LoLSpells",
        "type": "array"
      },
      "filter_over_LoLSpells": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "id": {
            "items": {
              "minimum": 1,
              "title": "LoLSpellID",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "name": {
            "items": {
              "title": "LoLSpellName",
              "type": "string"
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
      "range_over_LoLSpells": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "id": {
            "items": {
              "minimum": 1,
              "title": "LoLSpellID",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "name": {
            "items": {
              "title": "LoLSpellName",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          }
        },
        "type": "object"
      },
      "search_over_LoLSpells": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "name": {
            "title": "LoLSpellName",
            "type": "string"
          }
        },
        "type": "object"
      },
      "sort_over_LoLSpells": {
        "items": {
          "enum": [
            "id",
            "-id",
            "name",
            "-name"
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
    "/lol/spells": {
      "get": {
        "description": "List spells\n> ℹ️  \n> \n> This endpoint is available to all customers",
        "operationId": "get_lol_spells",
        "parameters": [
          {
            "description": "Options to filter results. String fields are case sensitive\nFor more information on filtering, see [docs](/docs/filtering-and-sorting#filter).",
            "explode": true,
            "in": "query",
            "name": "filter",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/filter_over_LoLSpells"
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
              "$ref": "#/components/schemas/range_over_LoLSpells"
            },
            "style": "deepObject"
          },
          {
            "description": "Options to sort results\nFor more information on sorting, see [docs](/docs/filtering-and-sorting#sort).",
            "in": "query",
            "name": "sort",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/sort_over_LoLSpells"
            }
          },
          {
            "description": "Options to search results\nFor more information on searching, see [docs](/docs/filtering-and-sorting#search).",
            "explode": true,
            "in": "query",
            "name": "search",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/search_over_LoLSpells"
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
            "$ref": "#/components/responses/LoLSpells"
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
        "summary": "List spells",
        "tags": [
          "LoL spells"
        ],
        "x-readme": {
          "code-samples": [
            {
              "code": "curl --request GET \\\n     --url 'https://api.pandascore.co/lol/spells' \\\n     --header 'accept: application/json'\n",
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