> ## Documentation Index
> Fetch the complete documentation index at: https://developers.pandascore.co/llms.txt
> Use this file to discover all available pages before exploring further.

# List Play-by-Play frames for a given game

List frames for a given League of Legends game
> ℹ️  
> 
> This endpoint is only available to customers with a real-time data plan

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
      "LoLGameFrames": {
        "content": {
          "application/json": {
            "examples": {
              "/lol/games/218606/frames?page[size]=1": {
                "description": "/lol/games/218606/frames?page[size]=1",
                "value": []
              }
            },
            "schema": {
              "$ref": "#/components/schemas/LoLGameFrames"
            }
          }
        },
        "description": "A list of League-of-Legends game frames"
      }
    },
    "schemas": {
      "LoLGameFrames": {
        "items": {
          "additionalProperties": false,
          "deprecated": false,
          "properties": {
            "blue": {
              "additionalProperties": false,
              "deprecated": false,
              "properties": {
                "acronym": {
                  "title": "TeamAcronym",
                  "type": "string"
                },
                "atakhans": {
                  "deprecated": false,
                  "description": "The number of Atakhan killed by a team.",
                  "maximum": 1,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLAtakhanKills",
                  "type": "integer"
                },
                "drakes": {
                  "minimum": 0,
                  "title": "LoLDragonKills",
                  "type": "integer"
                },
                "gold": {
                  "minimum": 0,
                  "title": "LoLGold",
                  "type": "integer"
                },
                "heralds": {
                  "deprecated": false,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLHeraldKills",
                  "type": "integer"
                },
                "id": {
                  "description": "The ID of the team.",
                  "minimum": 1,
                  "title": "TeamID",
                  "type": "integer"
                },
                "inhibitors": {
                  "description": "Number of inhibitors killed by the player",
                  "minimum": 0,
                  "title": "LoLInhibitorCount",
                  "type": "integer"
                },
                "kills": {
                  "minimum": 0,
                  "title": "LoLKillCount",
                  "type": "integer"
                },
                "name": {
                  "description": "The name of the team.",
                  "title": "TeamName",
                  "type": "string"
                },
                "nashors": {
                  "minimum": 0,
                  "title": "LoLBaronKills",
                  "type": "integer"
                },
                "players": {
                  "additionalProperties": false,
                  "deprecated": false,
                  "properties": {
                    "adc": {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "assists": {
                          "minimum": 0,
                          "title": "LoLAssistCount",
                          "type": "integer"
                        },
                        "champion": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
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
                            "name": {
                              "title": "LoLChampionName",
                              "type": "string"
                            },
                            "slug": {
                              "description": "Human-readable identifier of the champion.",
                              "title": "LoLChampionSlug",
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "image_url",
                            "name",
                            "slug"
                          ],
                          "title": "BaseLoLChampion",
                          "type": "object"
                        },
                        "cs": {
                          "description": "The player's Creep Score (CS.)\n\nNB: Creep Score can be different that the number of minions killed because neutral monsters can give more score.",
                          "minimum": 0,
                          "title": "LoLCreepScore",
                          "type": "integer"
                        },
                        "deaths": {
                          "minimum": 0,
                          "title": "LoLDeathCount",
                          "type": "integer"
                        },
                        "id": {
                          "description": "ID of the player",
                          "minimum": 1,
                          "title": "PlayerID",
                          "type": "integer"
                        },
                        "kills": {
                          "minimum": 0,
                          "title": "LoLKillCount",
                          "type": "integer"
                        },
                        "level": {
                          "minimum": 1,
                          "title": "LoLChampionLevel",
                          "type": "integer"
                        },
                        "name": {
                          "description": "Professional name of the player",
                          "title": "PlayerName",
                          "type": "string"
                        },
                        "summoner_spells": {
                          "items": {
                            "additionalProperties": false,
                            "deprecated": false,
                            "properties": {
                              "id": {
                                "minimum": 1,
                                "title": "LoLSpellID",
                                "type": "integer"
                              },
                              "name": {
                                "title": "LoLSpellName",
                                "type": "string"
                              }
                            },
                            "required": [
                              "id",
                              "name"
                            ],
                            "title": "BaseLoLSpell",
                            "type": "object"
                          },
                          "title": "BaseLoLSpells",
                          "type": "array"
                        }
                      },
                      "required": [
                        "assists",
                        "champion",
                        "cs",
                        "deaths",
                        "id",
                        "kills",
                        "level",
                        "name",
                        "summoner_spells"
                      ],
                      "title": "LoLPlayersRoleDetail",
                      "type": "object"
                    },
                    "jun": {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "assists": {
                          "minimum": 0,
                          "title": "LoLAssistCount",
                          "type": "integer"
                        },
                        "champion": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
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
                            "name": {
                              "title": "LoLChampionName",
                              "type": "string"
                            },
                            "slug": {
                              "description": "Human-readable identifier of the champion.",
                              "title": "LoLChampionSlug",
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "image_url",
                            "name",
                            "slug"
                          ],
                          "title": "BaseLoLChampion",
                          "type": "object"
                        },
                        "cs": {
                          "description": "The player's Creep Score (CS.)\n\nNB: Creep Score can be different that the number of minions killed because neutral monsters can give more score.",
                          "minimum": 0,
                          "title": "LoLCreepScore",
                          "type": "integer"
                        },
                        "deaths": {
                          "minimum": 0,
                          "title": "LoLDeathCount",
                          "type": "integer"
                        },
                        "id": {
                          "description": "ID of the player",
                          "minimum": 1,
                          "title": "PlayerID",
                          "type": "integer"
                        },
                        "kills": {
                          "minimum": 0,
                          "title": "LoLKillCount",
                          "type": "integer"
                        },
                        "level": {
                          "minimum": 1,
                          "title": "LoLChampionLevel",
                          "type": "integer"
                        },
                        "name": {
                          "description": "Professional name of the player",
                          "title": "PlayerName",
                          "type": "string"
                        },
                        "summoner_spells": {
                          "items": {
                            "additionalProperties": false,
                            "deprecated": false,
                            "properties": {
                              "id": {
                                "minimum": 1,
                                "title": "LoLSpellID",
                                "type": "integer"
                              },
                              "name": {
                                "title": "LoLSpellName",
                                "type": "string"
                              }
                            },
                            "required": [
                              "id",
                              "name"
                            ],
                            "title": "BaseLoLSpell",
                            "type": "object"
                          },
                          "title": "BaseLoLSpells",
                          "type": "array"
                        }
                      },
                      "required": [
                        "assists",
                        "champion",
                        "cs",
                        "deaths",
                        "id",
                        "kills",
                        "level",
                        "name",
                        "summoner_spells"
                      ],
                      "title": "LoLPlayersRoleDetail",
                      "type": "object"
                    },
                    "mid": {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "assists": {
                          "minimum": 0,
                          "title": "LoLAssistCount",
                          "type": "integer"
                        },
                        "champion": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
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
                            "name": {
                              "title": "LoLChampionName",
                              "type": "string"
                            },
                            "slug": {
                              "description": "Human-readable identifier of the champion.",
                              "title": "LoLChampionSlug",
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "image_url",
                            "name",
                            "slug"
                          ],
                          "title": "BaseLoLChampion",
                          "type": "object"
                        },
                        "cs": {
                          "description": "The player's Creep Score (CS.)\n\nNB: Creep Score can be different that the number of minions killed because neutral monsters can give more score.",
                          "minimum": 0,
                          "title": "LoLCreepScore",
                          "type": "integer"
                        },
                        "deaths": {
                          "minimum": 0,
                          "title": "LoLDeathCount",
                          "type": "integer"
                        },
                        "id": {
                          "description": "ID of the player",
                          "minimum": 1,
                          "title": "PlayerID",
                          "type": "integer"
                        },
                        "kills": {
                          "minimum": 0,
                          "title": "LoLKillCount",
                          "type": "integer"
                        },
                        "level": {
                          "minimum": 1,
                          "title": "LoLChampionLevel",
                          "type": "integer"
                        },
                        "name": {
                          "description": "Professional name of the player",
                          "title": "PlayerName",
                          "type": "string"
                        },
                        "summoner_spells": {
                          "items": {
                            "additionalProperties": false,
                            "deprecated": false,
                            "properties": {
                              "id": {
                                "minimum": 1,
                                "title": "LoLSpellID",
                                "type": "integer"
                              },
                              "name": {
                                "title": "LoLSpellName",
                                "type": "string"
                              }
                            },
                            "required": [
                              "id",
                              "name"
                            ],
                            "title": "BaseLoLSpell",
                            "type": "object"
                          },
                          "title": "BaseLoLSpells",
                          "type": "array"
                        }
                      },
                      "required": [
                        "assists",
                        "champion",
                        "cs",
                        "deaths",
                        "id",
                        "kills",
                        "level",
                        "name",
                        "summoner_spells"
                      ],
                      "title": "LoLPlayersRoleDetail",
                      "type": "object"
                    },
                    "sup": {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "assists": {
                          "minimum": 0,
                          "title": "LoLAssistCount",
                          "type": "integer"
                        },
                        "champion": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
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
                            "name": {
                              "title": "LoLChampionName",
                              "type": "string"
                            },
                            "slug": {
                              "description": "Human-readable identifier of the champion.",
                              "title": "LoLChampionSlug",
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "image_url",
                            "name",
                            "slug"
                          ],
                          "title": "BaseLoLChampion",
                          "type": "object"
                        },
                        "cs": {
                          "description": "The player's Creep Score (CS.)\n\nNB: Creep Score can be different that the number of minions killed because neutral monsters can give more score.",
                          "minimum": 0,
                          "title": "LoLCreepScore",
                          "type": "integer"
                        },
                        "deaths": {
                          "minimum": 0,
                          "title": "LoLDeathCount",
                          "type": "integer"
                        },
                        "id": {
                          "description": "ID of the player",
                          "minimum": 1,
                          "title": "PlayerID",
                          "type": "integer"
                        },
                        "kills": {
                          "minimum": 0,
                          "title": "LoLKillCount",
                          "type": "integer"
                        },
                        "level": {
                          "minimum": 1,
                          "title": "LoLChampionLevel",
                          "type": "integer"
                        },
                        "name": {
                          "description": "Professional name of the player",
                          "title": "PlayerName",
                          "type": "string"
                        },
                        "summoner_spells": {
                          "items": {
                            "additionalProperties": false,
                            "deprecated": false,
                            "properties": {
                              "id": {
                                "minimum": 1,
                                "title": "LoLSpellID",
                                "type": "integer"
                              },
                              "name": {
                                "title": "LoLSpellName",
                                "type": "string"
                              }
                            },
                            "required": [
                              "id",
                              "name"
                            ],
                            "title": "BaseLoLSpell",
                            "type": "object"
                          },
                          "title": "BaseLoLSpells",
                          "type": "array"
                        }
                      },
                      "required": [
                        "assists",
                        "champion",
                        "cs",
                        "deaths",
                        "id",
                        "kills",
                        "level",
                        "name",
                        "summoner_spells"
                      ],
                      "title": "LoLPlayersRoleDetail",
                      "type": "object"
                    },
                    "top": {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "assists": {
                          "minimum": 0,
                          "title": "LoLAssistCount",
                          "type": "integer"
                        },
                        "champion": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
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
                            "name": {
                              "title": "LoLChampionName",
                              "type": "string"
                            },
                            "slug": {
                              "description": "Human-readable identifier of the champion.",
                              "title": "LoLChampionSlug",
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "image_url",
                            "name",
                            "slug"
                          ],
                          "title": "BaseLoLChampion",
                          "type": "object"
                        },
                        "cs": {
                          "description": "The player's Creep Score (CS.)\n\nNB: Creep Score can be different that the number of minions killed because neutral monsters can give more score.",
                          "minimum": 0,
                          "title": "LoLCreepScore",
                          "type": "integer"
                        },
                        "deaths": {
                          "minimum": 0,
                          "title": "LoLDeathCount",
                          "type": "integer"
                        },
                        "id": {
                          "description": "ID of the player",
                          "minimum": 1,
                          "title": "PlayerID",
                          "type": "integer"
                        },
                        "kills": {
                          "minimum": 0,
                          "title": "LoLKillCount",
                          "type": "integer"
                        },
                        "level": {
                          "minimum": 1,
                          "title": "LoLChampionLevel",
                          "type": "integer"
                        },
                        "name": {
                          "description": "Professional name of the player",
                          "title": "PlayerName",
                          "type": "string"
                        },
                        "summoner_spells": {
                          "items": {
                            "additionalProperties": false,
                            "deprecated": false,
                            "properties": {
                              "id": {
                                "minimum": 1,
                                "title": "LoLSpellID",
                                "type": "integer"
                              },
                              "name": {
                                "title": "LoLSpellName",
                                "type": "string"
                              }
                            },
                            "required": [
                              "id",
                              "name"
                            ],
                            "title": "BaseLoLSpell",
                            "type": "object"
                          },
                          "title": "BaseLoLSpells",
                          "type": "array"
                        }
                      },
                      "required": [
                        "assists",
                        "champion",
                        "cs",
                        "deaths",
                        "id",
                        "kills",
                        "level",
                        "name",
                        "summoner_spells"
                      ],
                      "title": "LoLPlayersRoleDetail",
                      "type": "object"
                    }
                  },
                  "required": [
                    "adc",
                    "jun",
                    "mid",
                    "sup",
                    "top"
                  ],
                  "title": "LoLPlayersRole",
                  "type": "object"
                },
                "score": {
                  "minimum": 0,
                  "title": "MatchScore",
                  "type": "integer"
                },
                "towers": {
                  "minimum": 0,
                  "title": "LoLTowerKills",
                  "type": "integer"
                },
                "voidgrubs": {
                  "deprecated": false,
                  "description": "The number of voidgrubs killed by a team.",
                  "maximum": 6,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLVoidgrubKills",
                  "type": "integer"
                }
              },
              "required": [
                "acronym",
                "atakhans",
                "drakes",
                "gold",
                "heralds",
                "id",
                "inhibitors",
                "kills",
                "name",
                "nashors",
                "players",
                "score",
                "towers",
                "voidgrubs"
              ],
              "title": "LoLFrameTeam",
              "type": "object"
            },
            "current_timestamp": {
              "minimum": 0,
              "title": "InGameTimestamp",
              "type": "integer"
            },
            "game_id": {
              "description": "LoL game ID",
              "minimum": 1,
              "title": "LoLGameID",
              "type": "integer"
            },
            "match_id": {
              "minimum": 1,
              "title": "LoLMatchID",
              "type": "integer"
            },
            "red": {
              "additionalProperties": false,
              "deprecated": false,
              "properties": {
                "acronym": {
                  "title": "TeamAcronym",
                  "type": "string"
                },
                "atakhans": {
                  "deprecated": false,
                  "description": "The number of Atakhan killed by a team.",
                  "maximum": 1,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLAtakhanKills",
                  "type": "integer"
                },
                "drakes": {
                  "minimum": 0,
                  "title": "LoLDragonKills",
                  "type": "integer"
                },
                "gold": {
                  "minimum": 0,
                  "title": "LoLGold",
                  "type": "integer"
                },
                "heralds": {
                  "deprecated": false,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLHeraldKills",
                  "type": "integer"
                },
                "id": {
                  "description": "The ID of the team.",
                  "minimum": 1,
                  "title": "TeamID",
                  "type": "integer"
                },
                "inhibitors": {
                  "description": "Number of inhibitors killed by the player",
                  "minimum": 0,
                  "title": "LoLInhibitorCount",
                  "type": "integer"
                },
                "kills": {
                  "minimum": 0,
                  "title": "LoLKillCount",
                  "type": "integer"
                },
                "name": {
                  "description": "The name of the team.",
                  "title": "TeamName",
                  "type": "string"
                },
                "nashors": {
                  "minimum": 0,
                  "title": "LoLBaronKills",
                  "type": "integer"
                },
                "players": {
                  "additionalProperties": false,
                  "deprecated": false,
                  "properties": {
                    "adc": {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "assists": {
                          "minimum": 0,
                          "title": "LoLAssistCount",
                          "type": "integer"
                        },
                        "champion": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
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
                            "name": {
                              "title": "LoLChampionName",
                              "type": "string"
                            },
                            "slug": {
                              "description": "Human-readable identifier of the champion.",
                              "title": "LoLChampionSlug",
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "image_url",
                            "name",
                            "slug"
                          ],
                          "title": "BaseLoLChampion",
                          "type": "object"
                        },
                        "cs": {
                          "description": "The player's Creep Score (CS.)\n\nNB: Creep Score can be different that the number of minions killed because neutral monsters can give more score.",
                          "minimum": 0,
                          "title": "LoLCreepScore",
                          "type": "integer"
                        },
                        "deaths": {
                          "minimum": 0,
                          "title": "LoLDeathCount",
                          "type": "integer"
                        },
                        "id": {
                          "description": "ID of the player",
                          "minimum": 1,
                          "title": "PlayerID",
                          "type": "integer"
                        },
                        "kills": {
                          "minimum": 0,
                          "title": "LoLKillCount",
                          "type": "integer"
                        },
                        "level": {
                          "minimum": 1,
                          "title": "LoLChampionLevel",
                          "type": "integer"
                        },
                        "name": {
                          "description": "Professional name of the player",
                          "title": "PlayerName",
                          "type": "string"
                        },
                        "summoner_spells": {
                          "items": {
                            "additionalProperties": false,
                            "deprecated": false,
                            "properties": {
                              "id": {
                                "minimum": 1,
                                "title": "LoLSpellID",
                                "type": "integer"
                              },
                              "name": {
                                "title": "LoLSpellName",
                                "type": "string"
                              }
                            },
                            "required": [
                              "id",
                              "name"
                            ],
                            "title": "BaseLoLSpell",
                            "type": "object"
                          },
                          "title": "BaseLoLSpells",
                          "type": "array"
                        }
                      },
                      "required": [
                        "assists",
                        "champion",
                        "cs",
                        "deaths",
                        "id",
                        "kills",
                        "level",
                        "name",
                        "summoner_spells"
                      ],
                      "title": "LoLPlayersRoleDetail",
                      "type": "object"
                    },
                    "jun": {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "assists": {
                          "minimum": 0,
                          "title": "LoLAssistCount",
                          "type": "integer"
                        },
                        "champion": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
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
                            "name": {
                              "title": "LoLChampionName",
                              "type": "string"
                            },
                            "slug": {
                              "description": "Human-readable identifier of the champion.",
                              "title": "LoLChampionSlug",
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "image_url",
                            "name",
                            "slug"
                          ],
                          "title": "BaseLoLChampion",
                          "type": "object"
                        },
                        "cs": {
                          "description": "The player's Creep Score (CS.)\n\nNB: Creep Score can be different that the number of minions killed because neutral monsters can give more score.",
                          "minimum": 0,
                          "title": "LoLCreepScore",
                          "type": "integer"
                        },
                        "deaths": {
                          "minimum": 0,
                          "title": "LoLDeathCount",
                          "type": "integer"
                        },
                        "id": {
                          "description": "ID of the player",
                          "minimum": 1,
                          "title": "PlayerID",
                          "type": "integer"
                        },
                        "kills": {
                          "minimum": 0,
                          "title": "LoLKillCount",
                          "type": "integer"
                        },
                        "level": {
                          "minimum": 1,
                          "title": "LoLChampionLevel",
                          "type": "integer"
                        },
                        "name": {
                          "description": "Professional name of the player",
                          "title": "PlayerName",
                          "type": "string"
                        },
                        "summoner_spells": {
                          "items": {
                            "additionalProperties": false,
                            "deprecated": false,
                            "properties": {
                              "id": {
                                "minimum": 1,
                                "title": "LoLSpellID",
                                "type": "integer"
                              },
                              "name": {
                                "title": "LoLSpellName",
                                "type": "string"
                              }
                            },
                            "required": [
                              "id",
                              "name"
                            ],
                            "title": "BaseLoLSpell",
                            "type": "object"
                          },
                          "title": "BaseLoLSpells",
                          "type": "array"
                        }
                      },
                      "required": [
                        "assists",
                        "champion",
                        "cs",
                        "deaths",
                        "id",
                        "kills",
                        "level",
                        "name",
                        "summoner_spells"
                      ],
                      "title": "LoLPlayersRoleDetail",
                      "type": "object"
                    },
                    "mid": {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "assists": {
                          "minimum": 0,
                          "title": "LoLAssistCount",
                          "type": "integer"
                        },
                        "champion": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
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
                            "name": {
                              "title": "LoLChampionName",
                              "type": "string"
                            },
                            "slug": {
                              "description": "Human-readable identifier of the champion.",
                              "title": "LoLChampionSlug",
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "image_url",
                            "name",
                            "slug"
                          ],
                          "title": "BaseLoLChampion",
                          "type": "object"
                        },
                        "cs": {
                          "description": "The player's Creep Score (CS.)\n\nNB: Creep Score can be different that the number of minions killed because neutral monsters can give more score.",
                          "minimum": 0,
                          "title": "LoLCreepScore",
                          "type": "integer"
                        },
                        "deaths": {
                          "minimum": 0,
                          "title": "LoLDeathCount",
                          "type": "integer"
                        },
                        "id": {
                          "description": "ID of the player",
                          "minimum": 1,
                          "title": "PlayerID",
                          "type": "integer"
                        },
                        "kills": {
                          "minimum": 0,
                          "title": "LoLKillCount",
                          "type": "integer"
                        },
                        "level": {
                          "minimum": 1,
                          "title": "LoLChampionLevel",
                          "type": "integer"
                        },
                        "name": {
                          "description": "Professional name of the player",
                          "title": "PlayerName",
                          "type": "string"
                        },
                        "summoner_spells": {
                          "items": {
                            "additionalProperties": false,
                            "deprecated": false,
                            "properties": {
                              "id": {
                                "minimum": 1,
                                "title": "LoLSpellID",
                                "type": "integer"
                              },
                              "name": {
                                "title": "LoLSpellName",
                                "type": "string"
                              }
                            },
                            "required": [
                              "id",
                              "name"
                            ],
                            "title": "BaseLoLSpell",
                            "type": "object"
                          },
                          "title": "BaseLoLSpells",
                          "type": "array"
                        }
                      },
                      "required": [
                        "assists",
                        "champion",
                        "cs",
                        "deaths",
                        "id",
                        "kills",
                        "level",
                        "name",
                        "summoner_spells"
                      ],
                      "title": "LoLPlayersRoleDetail",
                      "type": "object"
                    },
                    "sup": {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "assists": {
                          "minimum": 0,
                          "title": "LoLAssistCount",
                          "type": "integer"
                        },
                        "champion": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
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
                            "name": {
                              "title": "LoLChampionName",
                              "type": "string"
                            },
                            "slug": {
                              "description": "Human-readable identifier of the champion.",
                              "title": "LoLChampionSlug",
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "image_url",
                            "name",
                            "slug"
                          ],
                          "title": "BaseLoLChampion",
                          "type": "object"
                        },
                        "cs": {
                          "description": "The player's Creep Score (CS.)\n\nNB: Creep Score can be different that the number of minions killed because neutral monsters can give more score.",
                          "minimum": 0,
                          "title": "LoLCreepScore",
                          "type": "integer"
                        },
                        "deaths": {
                          "minimum": 0,
                          "title": "LoLDeathCount",
                          "type": "integer"
                        },
                        "id": {
                          "description": "ID of the player",
                          "minimum": 1,
                          "title": "PlayerID",
                          "type": "integer"
                        },
                        "kills": {
                          "minimum": 0,
                          "title": "LoLKillCount",
                          "type": "integer"
                        },
                        "level": {
                          "minimum": 1,
                          "title": "LoLChampionLevel",
                          "type": "integer"
                        },
                        "name": {
                          "description": "Professional name of the player",
                          "title": "PlayerName",
                          "type": "string"
                        },
                        "summoner_spells": {
                          "items": {
                            "additionalProperties": false,
                            "deprecated": false,
                            "properties": {
                              "id": {
                                "minimum": 1,
                                "title": "LoLSpellID",
                                "type": "integer"
                              },
                              "name": {
                                "title": "LoLSpellName",
                                "type": "string"
                              }
                            },
                            "required": [
                              "id",
                              "name"
                            ],
                            "title": "BaseLoLSpell",
                            "type": "object"
                          },
                          "title": "BaseLoLSpells",
                          "type": "array"
                        }
                      },
                      "required": [
                        "assists",
                        "champion",
                        "cs",
                        "deaths",
                        "id",
                        "kills",
                        "level",
                        "name",
                        "summoner_spells"
                      ],
                      "title": "LoLPlayersRoleDetail",
                      "type": "object"
                    },
                    "top": {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "assists": {
                          "minimum": 0,
                          "title": "LoLAssistCount",
                          "type": "integer"
                        },
                        "champion": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
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
                            "name": {
                              "title": "LoLChampionName",
                              "type": "string"
                            },
                            "slug": {
                              "description": "Human-readable identifier of the champion.",
                              "title": "LoLChampionSlug",
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "image_url",
                            "name",
                            "slug"
                          ],
                          "title": "BaseLoLChampion",
                          "type": "object"
                        },
                        "cs": {
                          "description": "The player's Creep Score (CS.)\n\nNB: Creep Score can be different that the number of minions killed because neutral monsters can give more score.",
                          "minimum": 0,
                          "title": "LoLCreepScore",
                          "type": "integer"
                        },
                        "deaths": {
                          "minimum": 0,
                          "title": "LoLDeathCount",
                          "type": "integer"
                        },
                        "id": {
                          "description": "ID of the player",
                          "minimum": 1,
                          "title": "PlayerID",
                          "type": "integer"
                        },
                        "kills": {
                          "minimum": 0,
                          "title": "LoLKillCount",
                          "type": "integer"
                        },
                        "level": {
                          "minimum": 1,
                          "title": "LoLChampionLevel",
                          "type": "integer"
                        },
                        "name": {
                          "description": "Professional name of the player",
                          "title": "PlayerName",
                          "type": "string"
                        },
                        "summoner_spells": {
                          "items": {
                            "additionalProperties": false,
                            "deprecated": false,
                            "properties": {
                              "id": {
                                "minimum": 1,
                                "title": "LoLSpellID",
                                "type": "integer"
                              },
                              "name": {
                                "title": "LoLSpellName",
                                "type": "string"
                              }
                            },
                            "required": [
                              "id",
                              "name"
                            ],
                            "title": "BaseLoLSpell",
                            "type": "object"
                          },
                          "title": "BaseLoLSpells",
                          "type": "array"
                        }
                      },
                      "required": [
                        "assists",
                        "champion",
                        "cs",
                        "deaths",
                        "id",
                        "kills",
                        "level",
                        "name",
                        "summoner_spells"
                      ],
                      "title": "LoLPlayersRoleDetail",
                      "type": "object"
                    }
                  },
                  "required": [
                    "adc",
                    "jun",
                    "mid",
                    "sup",
                    "top"
                  ],
                  "title": "LoLPlayersRole",
                  "type": "object"
                },
                "score": {
                  "minimum": 0,
                  "title": "MatchScore",
                  "type": "integer"
                },
                "towers": {
                  "minimum": 0,
                  "title": "LoLTowerKills",
                  "type": "integer"
                },
                "voidgrubs": {
                  "deprecated": false,
                  "description": "The number of voidgrubs killed by a team.",
                  "maximum": 6,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLVoidgrubKills",
                  "type": "integer"
                }
              },
              "required": [
                "acronym",
                "atakhans",
                "drakes",
                "gold",
                "heralds",
                "id",
                "inhibitors",
                "kills",
                "name",
                "nashors",
                "players",
                "score",
                "towers",
                "voidgrubs"
              ],
              "title": "LoLFrameTeam",
              "type": "object"
            },
            "tournament_id": {
              "minimum": 1,
              "title": "TournamentID",
              "type": "integer"
            }
          },
          "required": [
            "blue",
            "current_timestamp",
            "game_id",
            "match_id",
            "red",
            "tournament_id"
          ],
          "title": "LoLGameFrame",
          "type": "object"
        },
        "title": "LoLGameFrames",
        "type": "array"
      },
      "LoLGameID": {
        "description": "LoL game ID",
        "minimum": 1,
        "title": "LoLGameID",
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
    "/lol/games/{lol_game_id}/frames": {
      "get": {
        "description": "List frames for a given League of Legends game\n> ℹ️  \n> \n> This endpoint is only available to customers with a real-time data plan",
        "operationId": "get_lol_games_lolGameId_frames",
        "parameters": [
          {
            "description": "A LoL game ID",
            "in": "path",
            "name": "lol_game_id",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/LoLGameID"
            }
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
            "$ref": "#/components/responses/LoLGameFrames"
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
        "summary": "List Play-by-Play frames for a given game",
        "tags": [
          "LoL games"
        ],
        "x-pandascore-plan": "Basic real-time plan",
        "x-readme": {
          "code-samples": [
            {
              "code": "curl --request GET \\\n     --url 'https://api.pandascore.co/lol/games/{lol_game_id}/frames' \\\n     --header 'accept: application/json'\n",
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