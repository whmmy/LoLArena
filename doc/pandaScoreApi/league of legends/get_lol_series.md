> ## Documentation Index
> Fetch the complete documentation index at: https://developers.pandascore.co/llms.txt
> Use this file to discover all available pages before exploring further.

# List LoL series

List series for the League of Legends videogame
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
      "LoLSeries": {
        "content": {
          "application/json": {
            "examples": {
              "/lol/series?page[size]=1": {
                "description": "/lol/series?page[size]=1",
                "value": [
                  {
                    "begin_at": "2025-01-13T05:00:00Z",
                    "end_at": "2025-02-27T14:00:00Z",
                    "full_name": "Kickoff 2025",
                    "id": 8889,
                    "league": {
                      "id": 4553,
                      "image_url": "https://cdn.pandascore.co/images/league/image/4553/LCK_CL_logo.png",
                      "modified_at": "2021-03-22T13:57:58Z",
                      "name": "LCK Challengers League",
                      "slug": "league-of-legends-lck-challengers-league",
                      "url": null
                    },
                    "league_id": 4553,
                    "modified_at": "2025-01-10T20:07:08Z",
                    "name": "Kickoff",
                    "season": null,
                    "slug": "league-of-legends-lck-challengers-league-kickoff-2025",
                    "tournaments": [
                      {
                        "begin_at": "2025-01-13T05:00:00Z",
                        "country": "KR",
                        "detailed_stats": true,
                        "end_at": "2025-02-27T14:00:00Z",
                        "has_bracket": false,
                        "id": 15742,
                        "league_id": 4553,
                        "live_supported": false,
                        "modified_at": "2025-01-12T14:56:10Z",
                        "name": "Group Stage",
                        "prizepool": null,
                        "region": "ASIA",
                        "serie_id": 8889,
                        "slug": "league-of-legends-lck-challengers-league-kickoff-2025-group-stage",
                        "tier": "c",
                        "type": "online",
                        "winner_id": null,
                        "winner_type": "Team"
                      },
                      {
                        "begin_at": "2025-02-10T08:00:00Z",
                        "country": null,
                        "detailed_stats": true,
                        "end_at": "2025-02-14T14:00:00Z",
                        "has_bracket": true,
                        "id": 15743,
                        "league_id": 4553,
                        "live_supported": false,
                        "modified_at": "2025-01-10T20:07:08Z",
                        "name": "Play-In",
                        "prizepool": null,
                        "region": "ASIA",
                        "serie_id": 8889,
                        "slug": "league-of-legends-lck-challengers-league-kickoff-2025-play-in",
                        "tier": "c",
                        "type": "online",
                        "winner_id": null,
                        "winner_type": "Team"
                      },
                      {
                        "begin_at": "2025-02-17T05:00:00Z",
                        "country": null,
                        "detailed_stats": true,
                        "end_at": "2025-02-27T14:00:00Z",
                        "has_bracket": true,
                        "id": 15744,
                        "league_id": 4553,
                        "live_supported": false,
                        "modified_at": "2025-01-10T20:07:08Z",
                        "name": "Playoffs",
                        "prizepool": null,
                        "region": "ASIA",
                        "serie_id": 8889,
                        "slug": "league-of-legends-lck-challengers-league-kickoff-2025-playoffs",
                        "tier": "c",
                        "type": "online",
                        "winner_id": null,
                        "winner_type": "Team"
                      }
                    ],
                    "videogame": {
                      "id": 1,
                      "name": "LoL",
                      "slug": "league-of-legends"
                    },
                    "videogame_title": null,
                    "winner_id": null,
                    "winner_type": "Team",
                    "year": 2025
                  }
                ]
              }
            },
            "schema": {
              "$ref": "#/components/schemas/LoLSeries"
            }
          }
        },
        "description": "A list of League-of-Legends series"
      }
    },
    "schemas": {
      "LoLSeries": {
        "items": {
          "additionalProperties": false,
          "deprecated": false,
          "description": "A serie, an occurrence of a league event",
          "properties": {
            "begin_at": {
              "deprecated": false,
              "format": "date-time",
              "minLength": 1,
              "nullable": true,
              "title": "SerieBeginAt",
              "type": "string"
            },
            "end_at": {
              "deprecated": false,
              "format": "date-time",
              "minLength": 1,
              "nullable": true,
              "title": "SerieEndAt",
              "type": "string"
            },
            "full_name": {
              "title": "SerieFullName",
              "type": "string"
            },
            "id": {
              "minimum": 1,
              "title": "SerieID",
              "type": "integer"
            },
            "league": {
              "additionalProperties": false,
              "deprecated": false,
              "properties": {
                "id": {
                  "minimum": 1,
                  "title": "LeagueID",
                  "type": "integer"
                },
                "image_url": {
                  "deprecated": false,
                  "format": "uri",
                  "nullable": true,
                  "title": "LeagueImageURL",
                  "type": "string"
                },
                "modified_at": {
                  "format": "date-time",
                  "minLength": 1,
                  "title": "LeagueModifiedAt",
                  "type": "string"
                },
                "name": {
                  "title": "LeagueName",
                  "type": "string"
                },
                "slug": {
                  "minLength": 1,
                  "pattern": "^[a-z0-9:_-]+$",
                  "title": "LeagueSlug",
                  "type": "string"
                },
                "url": {
                  "deprecated": false,
                  "format": "uri",
                  "nullable": true,
                  "title": "LeagueURL",
                  "type": "string"
                }
              },
              "required": [
                "id",
                "image_url",
                "modified_at",
                "name",
                "slug",
                "url"
              ],
              "title": "BaseLeague",
              "type": "object"
            },
            "league_id": {
              "minimum": 1,
              "title": "LeagueID",
              "type": "integer"
            },
            "modified_at": {
              "format": "date-time",
              "minLength": 1,
              "title": "SerieModifiedAt",
              "type": "string"
            },
            "name": {
              "deprecated": false,
              "nullable": true,
              "title": "SerieName",
              "type": "string"
            },
            "season": {
              "deprecated": false,
              "nullable": true,
              "title": "SerieSeason",
              "type": "string"
            },
            "slug": {
              "minLength": 1,
              "pattern": "^[a-z0-9_-]+$",
              "title": "SerieSlug",
              "type": "string"
            },
            "tournaments": {
              "items": {
                "additionalProperties": false,
                "deprecated": false,
                "properties": {
                  "begin_at": {
                    "deprecated": false,
                    "format": "date-time",
                    "minLength": 1,
                    "nullable": true,
                    "title": "TournamentBeginAt",
                    "type": "string"
                  },
                  "country": {
                    "deprecated": false,
                    "description": "Country code matching the location of the tournament according to the ISO 3166-1 standard (Alpha-2 code). In addition to the standard, the XK code is used for Kosovo. null if unknown",
                    "nullable": true,
                    "title": "TournamentCountry",
                    "type": "string"
                  },
                  "detailed_stats": {
                    "description": "Whether the tournament is expected to have detailed statistics available",
                    "title": "TournamentDetailedStats",
                    "type": "boolean"
                  },
                  "end_at": {
                    "deprecated": false,
                    "format": "date-time",
                    "minLength": 1,
                    "nullable": true,
                    "title": "TournamentEndAt",
                    "type": "string"
                  },
                  "has_bracket": {
                    "description": "Whether the tournament has a bracket",
                    "title": "TournamentHasBracket",
                    "type": "boolean"
                  },
                  "id": {
                    "minimum": 1,
                    "title": "TournamentID",
                    "type": "integer"
                  },
                  "league_id": {
                    "minimum": 1,
                    "title": "LeagueID",
                    "type": "integer"
                  },
                  "live_supported": {
                    "description": "Whether live is supported",
                    "title": "TournamentLiveSupported",
                    "type": "boolean"
                  },
                  "modified_at": {
                    "format": "date-time",
                    "minLength": 1,
                    "title": "TournamentModifiedAt",
                    "type": "string"
                  },
                  "name": {
                    "title": "TournamentName",
                    "type": "string"
                  },
                  "prizepool": {
                    "deprecated": false,
                    "nullable": true,
                    "title": "TournamentPrizepool",
                    "type": "string"
                  },
                  "region": {
                    "deprecated": false,
                    "description": "Region acronym for the location of the tournament.",
                    "enum": [
                      "AF",
                      "ASIA",
                      "EEU",
                      "ME",
                      "NA",
                      "OCE",
                      "SA",
                      "WEU"
                    ],
                    "nullable": true,
                    "title": "TournamentRegion",
                    "type": "string"
                  },
                  "serie_id": {
                    "minimum": 1,
                    "title": "SerieID",
                    "type": "integer"
                  },
                  "slug": {
                    "minLength": 1,
                    "pattern": "^[a-z0-9_-]+$",
                    "title": "TournamentSlug",
                    "type": "string"
                  },
                  "tier": {
                    "deprecated": false,
                    "description": "The tier of the tournament, ranging from 'S' to 'Unranked'. Ranking 'S' > 'A' > 'B' > 'C' > 'D' > 'Unranked'",
                    "enum": [
                      "a",
                      "b",
                      "c",
                      "d",
                      "s",
                      "unranked"
                    ],
                    "nullable": true,
                    "title": "TournamentTier",
                    "type": "string"
                  },
                  "type": {
                    "deprecated": false,
                    "description": "Location type for a tournament",
                    "enum": [
                      "offline",
                      "online",
                      "online/offline"
                    ],
                    "nullable": true,
                    "title": "TournamentLocationType",
                    "type": "string"
                  },
                  "winner_id": {
                    "anyOf": [
                      {
                        "description": "ID of the player",
                        "minimum": 1,
                        "title": "PlayerID",
                        "type": "integer"
                      },
                      {
                        "description": "The ID of the team.",
                        "minimum": 1,
                        "title": "TeamID",
                        "type": "integer"
                      }
                    ],
                    "deprecated": false,
                    "nullable": true,
                    "title": "OpponentID"
                  },
                  "winner_type": {
                    "deprecated": false,
                    "enum": [
                      "Player",
                      "Team"
                    ],
                    "nullable": true,
                    "title": "OpponentType",
                    "type": "string"
                  }
                },
                "required": [
                  "begin_at",
                  "country",
                  "detailed_stats",
                  "end_at",
                  "has_bracket",
                  "id",
                  "league_id",
                  "live_supported",
                  "modified_at",
                  "name",
                  "prizepool",
                  "region",
                  "serie_id",
                  "slug",
                  "tier",
                  "type",
                  "winner_id",
                  "winner_type"
                ],
                "title": "BaseTournament",
                "type": "object"
              },
              "title": "BaseTournaments",
              "type": "array"
            },
            "videogame": {
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
              "title": "CurrentVideogame",
              "type": "object"
            },
            "videogame_title": {
              "additionalProperties": false,
              "deprecated": false,
              "nullable": true,
              "properties": {
                "id": {
                  "minimum": 1,
                  "title": "VideogameTitleID",
                  "type": "integer"
                },
                "name": {
                  "title": "VideogameTitleName",
                  "type": "string"
                },
                "slug": {
                  "minLength": 1,
                  "pattern": "^[a-z0-9_-]+$",
                  "title": "VideogameTitleSlug",
                  "type": "string"
                },
                "videogame_id": {
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
                }
              },
              "required": [
                "id",
                "name",
                "slug",
                "videogame_id"
              ],
              "title": "VideogameTitle",
              "type": "object"
            },
            "winner_id": {
              "anyOf": [
                {
                  "description": "ID of the player",
                  "minimum": 1,
                  "title": "PlayerID",
                  "type": "integer"
                },
                {
                  "description": "The ID of the team.",
                  "minimum": 1,
                  "title": "TeamID",
                  "type": "integer"
                }
              ],
              "deprecated": false,
              "nullable": true,
              "title": "OpponentID"
            },
            "winner_type": {
              "deprecated": false,
              "enum": [
                "Player",
                "Team"
              ],
              "nullable": true,
              "title": "OpponentType",
              "type": "string"
            },
            "year": {
              "deprecated": false,
              "minimum": 2012,
              "nullable": true,
              "title": "SerieYear",
              "type": "integer"
            }
          },
          "required": [
            "begin_at",
            "end_at",
            "full_name",
            "id",
            "league",
            "league_id",
            "modified_at",
            "name",
            "season",
            "slug",
            "tournaments",
            "videogame",
            "videogame_title",
            "winner_id",
            "winner_type",
            "year"
          ],
          "title": "Serie",
          "type": "object"
        },
        "title": "LoLSeries",
        "type": "array"
      },
      "filter_over_LoLSeries": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "begin_at": {
            "items": {
              "format": "date-time",
              "minLength": 1,
              "title": "SerieBeginAt",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "end_at": {
            "items": {
              "format": "date-time",
              "minLength": 1,
              "title": "SerieEndAt",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "id": {
            "items": {
              "minimum": 1,
              "title": "SerieID",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "league_id": {
            "items": {
              "minimum": 1,
              "title": "LeagueID",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "modified_at": {
            "items": {
              "format": "date-time",
              "minLength": 1,
              "title": "SerieModifiedAt",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "name": {
            "items": {
              "title": "SerieName",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "season": {
            "items": {
              "title": "SerieSeason",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "slug": {
            "items": {
              "minLength": 1,
              "pattern": "^[a-z0-9_-]+$",
              "title": "SerieSlug",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "videogame_title": {
            "description": "A videogame title id or slug.\nOnly for `/csgo/*`, `/codmw/*`, `/fifa/*` and `/ow/*` endpoints\n",
            "items": {
              "oneOf": [
                {
                  "minimum": 1,
                  "title": "VideogameTitleID",
                  "type": "integer"
                },
                {
                  "minLength": 1,
                  "pattern": "^[a-z0-9_-]+$",
                  "title": "VideogameTitleSlug",
                  "type": "string"
                }
              ]
            },
            "minItems": 1,
            "type": "array"
          },
          "winner_id": {
            "items": {
              "anyOf": [
                {
                  "description": "ID of the player",
                  "minimum": 1,
                  "title": "PlayerID",
                  "type": "integer"
                },
                {
                  "description": "The ID of the team.",
                  "minimum": 1,
                  "title": "TeamID",
                  "type": "integer"
                }
              ],
              "title": "OpponentID"
            },
            "minItems": 1,
            "type": "array"
          },
          "winner_type": {
            "items": {
              "enum": [
                "Player",
                "Team"
              ],
              "title": "OpponentType",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "year": {
            "items": {
              "minimum": 2012,
              "title": "SerieYear",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          }
        },
        "type": "object"
      },
      "range_over_LoLSeries": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "begin_at": {
            "items": {
              "format": "date-time",
              "minLength": 1,
              "title": "SerieBeginAt",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "end_at": {
            "items": {
              "format": "date-time",
              "minLength": 1,
              "title": "SerieEndAt",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "id": {
            "items": {
              "minimum": 1,
              "title": "SerieID",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "league_id": {
            "items": {
              "minimum": 1,
              "title": "LeagueID",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "modified_at": {
            "items": {
              "format": "date-time",
              "minLength": 1,
              "title": "SerieModifiedAt",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "name": {
            "items": {
              "title": "SerieName",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "season": {
            "items": {
              "title": "SerieSeason",
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
              "title": "SerieSlug",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "winner_id": {
            "items": {
              "anyOf": [
                {
                  "description": "ID of the player",
                  "minimum": 1,
                  "title": "PlayerID",
                  "type": "integer"
                },
                {
                  "description": "The ID of the team.",
                  "minimum": 1,
                  "title": "TeamID",
                  "type": "integer"
                }
              ],
              "title": "OpponentID"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "winner_type": {
            "items": {
              "enum": [
                "Player",
                "Team"
              ],
              "title": "OpponentType",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "year": {
            "items": {
              "minimum": 2012,
              "title": "SerieYear",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          }
        },
        "type": "object"
      },
      "search_over_LoLSeries": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "name": {
            "title": "SerieName",
            "type": "string"
          },
          "season": {
            "title": "SerieSeason",
            "type": "string"
          },
          "slug": {
            "minLength": 1,
            "pattern": "^[a-z0-9_-]+$",
            "title": "SerieSlug",
            "type": "string"
          },
          "winner_type": {
            "enum": [
              "Player",
              "Team"
            ],
            "title": "OpponentType",
            "type": "string"
          }
        },
        "type": "object"
      },
      "sort_over_LoLSeries": {
        "items": {
          "enum": [
            "begin_at",
            "-begin_at",
            "end_at",
            "-end_at",
            "id",
            "-id",
            "league_id",
            "-league_id",
            "modified_at",
            "-modified_at",
            "name",
            "-name",
            "season",
            "-season",
            "slug",
            "-slug",
            "winner_id",
            "-winner_id",
            "winner_type",
            "-winner_type",
            "year",
            "-year"
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
    "/lol/series": {
      "get": {
        "description": "List series for the League of Legends videogame\n> ℹ️  \n> \n> This endpoint is available to all customers",
        "operationId": "get_lol_series",
        "parameters": [
          {
            "description": "Options to filter results. String fields are case sensitive\nFor more information on filtering, see [docs](/docs/filtering-and-sorting#filter).",
            "explode": true,
            "in": "query",
            "name": "filter",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/filter_over_LoLSeries"
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
              "$ref": "#/components/schemas/range_over_LoLSeries"
            },
            "style": "deepObject"
          },
          {
            "description": "Options to sort results\nFor more information on sorting, see [docs](/docs/filtering-and-sorting#sort).",
            "in": "query",
            "name": "sort",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/sort_over_LoLSeries"
            }
          },
          {
            "description": "Options to search results\nFor more information on searching, see [docs](/docs/filtering-and-sorting#search).",
            "explode": true,
            "in": "query",
            "name": "search",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/search_over_LoLSeries"
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
            "$ref": "#/components/responses/LoLSeries"
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
        "summary": "List LoL series",
        "tags": [
          "LoL series"
        ],
        "x-readme": {
          "code-samples": [
            {
              "code": "curl --request GET \\\n     --url 'https://api.pandascore.co/lol/series' \\\n     --header 'accept: application/json'\n",
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