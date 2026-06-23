> ## Documentation Index
> Fetch the complete documentation index at: https://developers.pandascore.co/llms.txt
> Use this file to discover all available pages before exploring further.

# List LoL runes

List the latest version of League of Legends (reforged) runes
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
      "LoLRunesReforged": {
        "content": {
          "application/json": {
            "examples": {
              "/lol/runes-reforged?page[size]=1": {
                "description": "/lol/runes-reforged?page[size]=1",
                "value": [
                  {
                    "id": 71,
                    "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/bd96d9ef-5102-4785-9a88-33d94e93a264.png",
                    "name": "Adaptative Force",
                    "type": "shard"
                  }
                ]
              }
            },
            "schema": {
              "$ref": "#/components/schemas/LoLRunesReforged"
            }
          }
        },
        "description": "A list of League-of-Legends (reforged) runes"
      }
    },
    "schemas": {
      "LoLRunesReforged": {
        "items": {
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
        "title": "LoLRunesReforged",
        "type": "array"
      },
      "filter_over_LoLRunesReforged": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "id": {
            "items": {
              "description": "ID of the rune",
              "minimum": 1,
              "title": "LoLRuneReforgedID",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "name": {
            "items": {
              "description": "Name of the rune path",
              "title": "LoLRuneReforgedName",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          }
        },
        "type": "object"
      },
      "range_over_LoLRunesReforged": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "id": {
            "items": {
              "description": "ID of the rune",
              "minimum": 1,
              "title": "LoLRuneReforgedID",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "name": {
            "items": {
              "description": "Name of the rune path",
              "title": "LoLRuneReforgedName",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          }
        },
        "type": "object"
      },
      "search_over_LoLRunesReforged": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "name": {
            "description": "Name of the rune path",
            "title": "LoLRuneReforgedName",
            "type": "string"
          }
        },
        "type": "object"
      },
      "sort_over_LoLRunesReforged": {
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
    "/lol/runes-reforged": {
      "get": {
        "description": "List the latest version of League of Legends (reforged) runes\n> ℹ️  \n> \n> This endpoint is available to all customers",
        "operationId": "get_lol_runes-reforged",
        "parameters": [
          {
            "description": "Options to filter results. String fields are case sensitive\nFor more information on filtering, see [docs](/docs/filtering-and-sorting#filter).",
            "explode": true,
            "in": "query",
            "name": "filter",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/filter_over_LoLRunesReforged"
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
              "$ref": "#/components/schemas/range_over_LoLRunesReforged"
            },
            "style": "deepObject"
          },
          {
            "description": "Options to sort results\nFor more information on sorting, see [docs](/docs/filtering-and-sorting#sort).",
            "in": "query",
            "name": "sort",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/sort_over_LoLRunesReforged"
            }
          },
          {
            "description": "Options to search results\nFor more information on searching, see [docs](/docs/filtering-and-sorting#search).",
            "explode": true,
            "in": "query",
            "name": "search",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/search_over_LoLRunesReforged"
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
            "$ref": "#/components/responses/LoLRunesReforged"
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
        "summary": "List LoL runes",
        "tags": [
          "LoL runes"
        ],
        "x-readme": {
          "code-samples": [
            {
              "code": "curl --request GET \\\n     --url 'https://api.pandascore.co/lol/runes-reforged' \\\n     --header 'accept: application/json'\n",
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