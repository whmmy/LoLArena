> ## Documentation Index
> Fetch the complete documentation index at: https://developers.pandascore.co/llms.txt
> Use this file to discover all available pages before exploring further.

# List LoL teams

List teams for the League of Legends videogame
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
      "LoLTeams": {
        "content": {
          "application/json": {
            "examples": {
              "/lol/teams?page[size]=1": {
                "description": "/lol/teams?page[size]=1",
                "value": [
                  {
                    "acronym": "IE",
                    "current_videogame": {
                      "id": 1,
                      "name": "LoL",
                      "slug": "league-of-legends"
                    },
                    "dark_mode_image_url": "https://cdn.pandascore.co/dark_images/team/dark_image/137465/inferno_esports__2528_filipino_team_2529logo_square.png",
                    "id": 137465,
                    "image_url": "https://cdn.pandascore.co/images/team/image/137465/inferno_esports__2528_filipino_team_2529logo_square.png",
                    "location": "PH",
                    "modified_at": "2025-10-03T09:35:13Z",
                    "name": "Inferno Esports",
                    "players": [
                      {
                        "active": true,
                        "age": null,
                        "birthday": null,
                        "first_name": null,
                        "id": 38389,
                        "image_url": null,
                        "last_name": null,
                        "modified_at": "2025-10-03T07:36:33Z",
                        "name": "Austerity",
                        "nationality": "PH",
                        "role": "adc",
                        "slug": "austerity"
                      },
                      {
                        "active": true,
                        "age": null,
                        "birthday": null,
                        "first_name": "Marc",
                        "id": 62066,
                        "image_url": "https://cdn.pandascore.co/images/player/image/62066/ie_moopz_lcp_wc_2025.png",
                        "last_name": "Jazztine Barrion",
                        "modified_at": "2025-10-03T09:34:10Z",
                        "name": "moopz",
                        "nationality": "PH",
                        "role": "sup",
                        "slug": "moopz-marc-jazztine-barrion"
                      },
                      {
                        "active": true,
                        "age": null,
                        "birthday": null,
                        "first_name": "Karl Justin",
                        "id": 62067,
                        "image_url": "https://cdn.pandascore.co/images/player/image/62067/ie_krimson_lcp_wc_2025.png",
                        "last_name": "Guevarra",
                        "modified_at": "2025-10-03T09:34:10Z",
                        "name": "Krimson",
                        "nationality": "PH",
                        "role": "mid",
                        "slug": "krimson-karl-justin-guevarra"
                      },
                      {
                        "active": true,
                        "age": null,
                        "birthday": null,
                        "first_name": "Lee Jack",
                        "id": 62068,
                        "image_url": null,
                        "last_name": "Wei",
                        "modified_at": "2025-10-03T09:38:09Z",
                        "name": "1jw",
                        "nationality": "MY",
                        "role": "top",
                        "slug": "1jw"
                      },
                      {
                        "active": true,
                        "age": 24,
                        "birthday": "2001-05-15",
                        "first_name": "Ong",
                        "id": 62069,
                        "image_url": "https://cdn.pandascore.co/images/player/image/62069/ie_born_this_way_lcp_wc_2025.png",
                        "last_name": "Ting Yi",
                        "modified_at": "2025-10-03T09:36:58Z",
                        "name": "BornThisWay",
                        "nationality": "MY",
                        "role": "jun",
                        "slug": "bornthisway"
                      },
                      {
                        "active": true,
                        "age": 21,
                        "birthday": "2004-04-20",
                        "first_name": "Christian",
                        "id": 62070,
                        "image_url": "https://cdn.pandascore.co/images/player/image/62070/ie_celest_lcp_wc_25.png",
                        "last_name": "Grecia",
                        "modified_at": "2025-10-03T09:39:06Z",
                        "name": "Celest",
                        "nationality": "MY",
                        "role": "mid",
                        "slug": "celest"
                      }
                    ],
                    "slug": "inferno-esports"
                  }
                ]
              }
            },
            "schema": {
              "$ref": "#/components/schemas/LoLTeams"
            }
          }
        },
        "description": "A list of League-of-Legends teams"
      }
    },
    "schemas": {
      "LoLTeams": {
        "items": {
          "additionalProperties": false,
          "deprecated": false,
          "properties": {
            "acronym": {
              "deprecated": false,
              "nullable": true,
              "title": "TeamAcronym",
              "type": "string"
            },
            "current_videogame": {
              "deprecated": false,
              "enum": [
                {
                  "id": 1,
                  "name": "LoL",
                  "slug": "league-of-legends"
                },
                {
                  "id": 3,
                  "name": "Counter-Strike",
                  "slug": "cs-go"
                },
                {
                  "id": 4,
                  "name": "Dota 2",
                  "slug": "dota-2"
                },
                {
                  "id": 14,
                  "name": "Overwatch",
                  "slug": "ow"
                },
                {
                  "id": 20,
                  "name": "PUBG",
                  "slug": "pubg"
                },
                {
                  "id": 22,
                  "name": "Rocket League",
                  "slug": "rl"
                },
                {
                  "id": 23,
                  "name": "Call of Duty",
                  "slug": "cod-mw"
                },
                {
                  "id": 24,
                  "name": "Rainbow 6 Siege",
                  "slug": "r6-siege"
                },
                {
                  "id": 25,
                  "name": "EA Sports FC",
                  "slug": "fifa"
                },
                {
                  "id": 26,
                  "name": "Valorant",
                  "slug": "valorant"
                },
                {
                  "id": 27,
                  "name": "King of Glory",
                  "slug": "kog"
                },
                {
                  "id": 28,
                  "name": "LoL Wild Rift",
                  "slug": "lol-wild-rift"
                },
                {
                  "id": 29,
                  "name": "StarCraft 2",
                  "slug": "starcraft-2"
                },
                {
                  "id": 30,
                  "name": "StarCraft Brood War",
                  "slug": "starcraft-brood-war"
                },
                {
                  "id": 31,
                  "name": "eSoccer",
                  "slug": "e-soccer"
                },
                {
                  "id": 32,
                  "name": "eBasketball",
                  "slug": "e-basketball"
                },
                {
                  "id": 33,
                  "name": "eCricket",
                  "slug": "e-cricket"
                },
                {
                  "id": 34,
                  "name": "Mobile Legends: Bang Bang",
                  "slug": "mlbb"
                },
                {
                  "id": 35,
                  "name": "eHockey",
                  "slug": "e-hockey"
                },
                {
                  "id": 36,
                  "name": "eTennis",
                  "slug": "e-tennis"
                }
              ],
              "nullable": true,
              "title": "CurrentVideogame",
              "type": "object"
            },
            "dark_mode_image_url": {
              "deprecated": false,
              "description": "URL of the team logo",
              "format": "uri",
              "nullable": true,
              "title": "TeamImageURL",
              "type": "string"
            },
            "id": {
              "description": "The ID of the team.",
              "minimum": 1,
              "title": "TeamID",
              "type": "integer"
            },
            "image_url": {
              "deprecated": false,
              "description": "URL of the team logo",
              "format": "uri",
              "nullable": true,
              "title": "TeamImageURL",
              "type": "string"
            },
            "location": {
              "deprecated": false,
              "description": "The team's organization location",
              "nullable": true,
              "title": "TeamLocation",
              "type": "string"
            },
            "modified_at": {
              "format": "date-time",
              "minLength": 1,
              "title": "TeamModifiedAt",
              "type": "string"
            },
            "name": {
              "description": "The name of the team.",
              "title": "TeamName",
              "type": "string"
            },
            "players": {
              "items": {
                "additionalProperties": false,
                "deprecated": false,
                "properties": {
                  "active": {
                    "description": "Whether player is active",
                    "title": "PlayerIsActive",
                    "type": "boolean"
                  },
                  "age": {
                    "deprecated": false,
                    "description": "Age of the player, `null` if unknown. When `birthday` is `null`, `age` is an approxiamation. Read more about [players' age](/docs/about-players-age)\n**Note**: This field is only present for users running the Historical plan or above.",
                    "minimum": 0,
                    "nullable": true,
                    "title": "PlayerAge",
                    "type": "number"
                  },
                  "birthday": {
                    "deprecated": false,
                    "description": "Birth day of the player, `YYYY-MM-DD` format. `null` if unknown.\n**Note**: This field is only present for users running the Historical plan or above.",
                    "nullable": true,
                    "title": "PlayerBirthday",
                    "type": "string"
                  },
                  "first_name": {
                    "deprecated": false,
                    "description": "First name of the player. `null` if unknown",
                    "nullable": true,
                    "title": "PlayerFirstName",
                    "type": "string"
                  },
                  "id": {
                    "description": "ID of the player",
                    "minimum": 1,
                    "title": "PlayerID",
                    "type": "integer"
                  },
                  "image_url": {
                    "deprecated": false,
                    "description": "URL to the photo of the player. `null` if not available.",
                    "format": "uri",
                    "nullable": true,
                    "title": "PlayerImageURL",
                    "type": "string"
                  },
                  "last_name": {
                    "deprecated": false,
                    "description": "Last name of the player. `null` if unknown",
                    "nullable": true,
                    "title": "PlayerLastName",
                    "type": "string"
                  },
                  "modified_at": {
                    "format": "date-time",
                    "minLength": 1,
                    "title": "PlayerModifiedAt",
                    "type": "string"
                  },
                  "name": {
                    "description": "Professional name of the player",
                    "title": "PlayerName",
                    "type": "string"
                  },
                  "nationality": {
                    "deprecated": false,
                    "description": "Country code matching the nationality of the player according to the ISO 3166-1 standard (Alpha-2 code).\nIn addition to the standard, the `XK` code is used for Kosovo.\n`null` if unknown",
                    "nullable": true,
                    "title": "PlayerNationality",
                    "type": "string"
                  },
                  "role": {
                    "deprecated": false,
                    "description": "Role/position of the player. Field value varies depending on the video game.`null` if unknown.\n**Note**: role is only available for DotA 2, League of Legends, and Overwatch players.\n`null` for other video games.",
                    "nullable": true,
                    "title": "PlayerRoleSlug",
                    "type": "string"
                  },
                  "slug": {
                    "deprecated": false,
                    "description": "Unique, human-readable identifier for the player.\n`id` and `slug` can be used interchangeably throughout the API.",
                    "minLength": 1,
                    "nullable": true,
                    "pattern": "^[a-z0-9_-]+$",
                    "title": "PlayerSlug",
                    "type": "string"
                  }
                },
                "required": [
                  "active",
                  "age",
                  "birthday",
                  "first_name",
                  "id",
                  "image_url",
                  "last_name",
                  "modified_at",
                  "name",
                  "nationality",
                  "role",
                  "slug"
                ],
                "title": "BasePlayer",
                "type": "object"
              },
              "title": "BasePlayers",
              "type": "array"
            },
            "slug": {
              "deprecated": false,
              "minLength": 1,
              "nullable": true,
              "pattern": "^[a-z0-9_-]+$",
              "title": "TeamSlug",
              "type": "string"
            }
          },
          "required": [
            "acronym",
            "current_videogame",
            "dark_mode_image_url",
            "id",
            "image_url",
            "location",
            "modified_at",
            "name",
            "players",
            "slug"
          ],
          "title": "Team",
          "type": "object"
        },
        "title": "LoLTeams",
        "type": "array"
      },
      "filter_over_LoLTeams": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "acronym": {
            "items": {
              "title": "TeamAcronym",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "id": {
            "items": {
              "description": "The ID of the team.",
              "minimum": 1,
              "title": "TeamID",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "location": {
            "items": {
              "description": "The team's organization location",
              "title": "TeamLocation",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "modified_at": {
            "items": {
              "format": "date-time",
              "minLength": 1,
              "title": "TeamModifiedAt",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "name": {
            "items": {
              "description": "The name of the team.",
              "title": "TeamName",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "slug": {
            "items": {
              "minLength": 1,
              "pattern": "^[a-z0-9_-]+$",
              "title": "TeamSlug",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "videogame_id": {
            "items": {
              "description": "A videogame ID",
              "enum": [
                1,
                3,
                4,
                14,
                20,
                22,
                23,
                24,
                25,
                26,
                27,
                28,
                29,
                30,
                31,
                32,
                33,
                34,
                35,
                36
              ],
              "title": "VideogameID",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          }
        },
        "type": "object"
      },
      "range_over_LoLTeams": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "acronym": {
            "items": {
              "title": "TeamAcronym",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "id": {
            "items": {
              "description": "The ID of the team.",
              "minimum": 1,
              "title": "TeamID",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "location": {
            "items": {
              "description": "The team's organization location",
              "title": "TeamLocation",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "modified_at": {
            "items": {
              "format": "date-time",
              "minLength": 1,
              "title": "TeamModifiedAt",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "name": {
            "items": {
              "description": "The name of the team.",
              "title": "TeamName",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "slug": {
            "items": {
              "minLength": 1,
              "pattern": "^[a-z0-9_-]+$",
              "title": "TeamSlug",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          }
        },
        "type": "object"
      },
      "search_over_LoLTeams": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "acronym": {
            "title": "TeamAcronym",
            "type": "string"
          },
          "location": {
            "description": "The team's organization location",
            "title": "TeamLocation",
            "type": "string"
          },
          "name": {
            "description": "The name of the team.",
            "title": "TeamName",
            "type": "string"
          },
          "slug": {
            "minLength": 1,
            "pattern": "^[a-z0-9_-]+$",
            "title": "TeamSlug",
            "type": "string"
          }
        },
        "type": "object"
      },
      "sort_over_LoLTeams": {
        "items": {
          "enum": [
            "acronym",
            "-acronym",
            "id",
            "-id",
            "location",
            "-location",
            "modified_at",
            "-modified_at",
            "name",
            "-name",
            "slug",
            "-slug",
            "videogame_id",
            "-videogame_id"
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
    "/lol/teams": {
      "get": {
        "description": "List teams for the League of Legends videogame\n> ℹ️  \n> \n> This endpoint is available to all customers",
        "operationId": "get_lol_teams",
        "parameters": [
          {
            "description": "Options to filter results. String fields are case sensitive\nFor more information on filtering, see [docs](/docs/filtering-and-sorting#filter).",
            "explode": true,
            "in": "query",
            "name": "filter",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/filter_over_LoLTeams"
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
              "$ref": "#/components/schemas/range_over_LoLTeams"
            },
            "style": "deepObject"
          },
          {
            "description": "Options to sort results\nFor more information on sorting, see [docs](/docs/filtering-and-sorting#sort).",
            "in": "query",
            "name": "sort",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/sort_over_LoLTeams"
            }
          },
          {
            "description": "Options to search results\nFor more information on searching, see [docs](/docs/filtering-and-sorting#search).",
            "explode": true,
            "in": "query",
            "name": "search",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/search_over_LoLTeams"
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
            "$ref": "#/components/responses/LoLTeams"
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
        "summary": "List LoL teams",
        "tags": [
          "LoL teams"
        ],
        "x-readme": {
          "code-samples": [
            {
              "code": "curl --request GET \\\n     --url 'https://api.pandascore.co/lol/teams' \\\n     --header 'accept: application/json'\n",
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