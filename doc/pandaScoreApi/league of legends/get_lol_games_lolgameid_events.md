> ## Documentation Index
> Fetch the complete documentation index at: https://developers.pandascore.co/llms.txt
> Use this file to discover all available pages before exploring further.

# List Play-by-Play events for a given game

List events for a given League of Legends game
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
      "LoLGameEvents": {
        "content": {
          "application/json": {
            "examples": {
              "Drake kill": {
                "description": "/lol/games/243129/events?page[size]=1",
                "value": [
                  {
                    "game_id": 243129,
                    "ingame_timestamp": 210,
                    "is_first": true,
                    "match_id": 720982,
                    "payload": {
                      "assists": [
                        {
                          "object": {
                            "champion": {
                              "id": 3121,
                              "name": "Viktor"
                            },
                            "player_id": 1429,
                            "player_name": "Larssen",
                            "side": "red"
                          },
                          "type": "player"
                        }
                      ],
                      "killer": {
                        "object": {
                          "champion": {
                            "id": 3085,
                            "name": "Sejuani"
                          },
                          "player_id": 2538,
                          "player_name": "Malrang",
                          "side": "red"
                        },
                        "type": "player"
                      },
                      "victim": {
                        "object": {
                          "champion": {
                            "id": 3247,
                            "name": "Jayce"
                          },
                          "player_id": 1132,
                          "player_name": "Caps",
                          "side": "blue"
                        },
                        "type": "player"
                      }
                    },
                    "tournament_id": 9913,
                    "type": "player_kill"
                  }
                ]
              },
              "Player kill": {
                "description": "/lol/games/243129/events?page[size]=1&page[number]=2",
                "value": [
                  {
                    "game_id": 243129,
                    "ingame_timestamp": 353,
                    "is_first": false,
                    "match_id": 720982,
                    "payload": {
                      "assists": [
                        {
                          "object": {
                            "champion": {
                              "id": 3085,
                              "name": "Sejuani"
                            },
                            "player_id": 2538,
                            "player_name": "Malrang",
                            "side": "red"
                          },
                          "type": "player"
                        }
                      ],
                      "killer": {
                        "object": {
                          "champion": {
                            "id": 3121,
                            "name": "Viktor"
                          },
                          "player_id": 1429,
                          "player_name": "Larssen",
                          "side": "red"
                        },
                        "type": "player"
                      },
                      "victim": {
                        "object": {
                          "champion": {
                            "id": 3247,
                            "name": "Jayce"
                          },
                          "player_id": 1132,
                          "player_name": "Caps",
                          "side": "blue"
                        },
                        "type": "player"
                      }
                    },
                    "tournament_id": 9913,
                    "type": "player_kill"
                  }
                ]
              },
              "Rift herald kill": {
                "description": "/lol/games/217505/events?per_page=1&page=7",
                "value": [
                  {
                    "game_id": 217505,
                    "ingame_timestamp": 548,
                    "is_first": false,
                    "match_id": 564561,
                    "payload": {
                      "assists": [],
                      "killer": {
                        "object": {
                          "champion": {
                            "id": 2615,
                            "name": "Sett"
                          },
                          "player_id": 15344,
                          "player_name": "Xuhao",
                          "side": "blue"
                        },
                        "type": "player"
                      },
                      "victim": {
                        "object": {
                          "name": "Rift Herald"
                        },
                        "type": "rift_herald"
                      }
                    },
                    "tournament_id": 4153,
                    "type": "rift_herald_kill"
                  }
                ]
              },
              "Tower kill": {
                "description": "/lol/games/243129/events?page[size]=1&page[number]=11",
                "value": [
                  {
                    "game_id": 243129,
                    "ingame_timestamp": 956,
                    "is_first": false,
                    "match_id": 720982,
                    "payload": {
                      "assists": [
                        {
                          "object": {
                            "champion": {
                              "id": 3221,
                              "name": "Nautilus"
                            },
                            "player_id": 605,
                            "player_name": "Mikyx",
                            "side": "blue"
                          },
                          "type": "player"
                        },
                        {
                          "object": {
                            "champion": {
                              "id": 3053,
                              "name": "Maokai"
                            },
                            "player_id": 31994,
                            "player_name": "Yike",
                            "side": "blue"
                          },
                          "type": "player"
                        }
                      ],
                      "killer": {
                        "object": {
                          "champion": {
                            "id": 3219,
                            "name": "Miss Fortune"
                          },
                          "player_id": 871,
                          "player_name": "Hans sama",
                          "side": "blue"
                        },
                        "type": "player"
                      },
                      "victim": {
                        "object": {
                          "champion": {
                            "id": 3215,
                            "name": "Lucian"
                          },
                          "player_id": 21577,
                          "player_name": "Comp",
                          "side": "red"
                        },
                        "type": "player"
                      }
                    },
                    "tournament_id": 9913,
                    "type": "player_kill"
                  }
                ]
              }
            },
            "schema": {
              "$ref": "#/components/schemas/LoLGameEvents"
            }
          }
        },
        "description": "A list of League-of-Legends game events"
      }
    },
    "schemas": {
      "LoLGameEvents": {
        "items": {
          "additionalProperties": false,
          "deprecated": false,
          "properties": {
            "game_id": {
              "description": "LoL game ID",
              "minimum": 1,
              "title": "LoLGameID",
              "type": "integer"
            },
            "ingame_timestamp": {
              "minimum": 0,
              "title": "InGameTimestamp",
              "type": "integer"
            },
            "is_first": {
              "description": "Whether event is first of its kind to happen",
              "title": "LoLIsFirstEvent",
              "type": "boolean"
            },
            "match_id": {
              "minimum": 1,
              "title": "LoLMatchID",
              "type": "integer"
            },
            "payload": {
              "additionalProperties": false,
              "deprecated": false,
              "properties": {
                "assists": {
                  "items": {
                    "additionalProperties": false,
                    "deprecated": false,
                    "properties": {
                      "object": {
                        "additionalProperties": false,
                        "deprecated": false,
                        "properties": {
                          "champion": {
                            "additionalProperties": false,
                            "deprecated": false,
                            "properties": {
                              "id": {
                                "minimum": 1,
                                "title": "LoLChampionID",
                                "type": "integer"
                              },
                              "name": {
                                "title": "LoLChampionName",
                                "type": "string"
                              }
                            },
                            "required": [
                              "id",
                              "name"
                            ],
                            "title": "LoLEventChampion",
                            "type": "object"
                          },
                          "player_id": {
                            "description": "ID of the player",
                            "minimum": 1,
                            "title": "PlayerID",
                            "type": "integer"
                          },
                          "player_name": {
                            "description": "Professional name of the player",
                            "title": "PlayerName",
                            "type": "string"
                          },
                          "side": {
                            "enum": [
                              "blue",
                              "red"
                            ],
                            "title": "LoLTeamColor",
                            "type": "string"
                          }
                        },
                        "required": [
                          "champion",
                          "player_id",
                          "player_name",
                          "side"
                        ],
                        "title": "LoLEventPlayerObject",
                        "type": "object"
                      },
                      "type": {
                        "enum": [
                          "player"
                        ],
                        "type": "string"
                      }
                    },
                    "required": [
                      "object",
                      "type"
                    ],
                    "title": "LoLEventPlayer",
                    "type": "object"
                  },
                  "title": "LoLEventAssists",
                  "type": "array"
                },
                "killer": {
                  "oneOf": [
                    {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "object": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
                            "name": {
                              "enum": [
                                "Atakhan"
                              ],
                              "title": "LoLEventAtakhanValue",
                              "type": "string"
                            }
                          },
                          "required": [
                            "name"
                          ],
                          "title": "LoLEventAtakhanObject",
                          "type": "object"
                        },
                        "type": {
                          "enum": [
                            "atakhan"
                          ],
                          "type": "string"
                        }
                      },
                      "required": [
                        "object",
                        "type"
                      ],
                      "title": "LoLEventAtakhan",
                      "type": "object"
                    },
                    {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "object": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
                            "name": {
                              "enum": [
                                "Chemtech Drake",
                                "Cloud Drake",
                                "Elder Drake",
                                "Hextech Drake",
                                "Infernal Drake",
                                "Mountain Drake",
                                "Ocean Drake"
                              ],
                              "title": "LoLDrakeName",
                              "type": "string"
                            },
                            "type": {
                              "enum": [
                                "chemtech",
                                "cloud",
                                "elder",
                                "hextech",
                                "infernal",
                                "mountain",
                                "ocean"
                              ],
                              "title": "LoLDrakeType",
                              "type": "string"
                            }
                          },
                          "required": [
                            "name",
                            "type"
                          ],
                          "title": "LoLEventDrakeObject",
                          "type": "object"
                        },
                        "type": {
                          "enum": [
                            "drake"
                          ],
                          "type": "string"
                        }
                      },
                      "required": [
                        "object",
                        "type"
                      ],
                      "title": "LoLEventDrake",
                      "type": "object"
                    },
                    {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "object": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
                            "name": {
                              "enum": [
                                "Rift Herald",
                                "riftherald"
                              ],
                              "title": "LoLEventHeraldValue",
                              "type": "string"
                            }
                          },
                          "required": [
                            "name"
                          ],
                          "title": "LoLEventHeraldObject",
                          "type": "object"
                        },
                        "type": {
                          "enum": [
                            "herald",
                            "rift_herald"
                          ],
                          "type": "string"
                        }
                      },
                      "required": [
                        "object",
                        "type"
                      ],
                      "title": "LoLEventHerald",
                      "type": "object"
                    },
                    {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "object": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
                            "name": {
                              "enum": [
                                "Minion"
                              ],
                              "title": "LoLEventMinionValue",
                              "type": "string"
                            },
                            "side": {
                              "enum": [
                                "blue",
                                "red"
                              ],
                              "title": "LoLTeamColor",
                              "type": "string"
                            }
                          },
                          "required": [
                            "name",
                            "side"
                          ],
                          "title": "LoLEventMinionObject",
                          "type": "object"
                        },
                        "type": {
                          "enum": [
                            "minion"
                          ],
                          "type": "string"
                        }
                      },
                      "required": [
                        "object",
                        "type"
                      ],
                      "title": "LoLEventMinion",
                      "type": "object"
                    },
                    {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "object": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
                            "name": {
                              "enum": [
                                "Baron Nashor"
                              ],
                              "title": "LoLEventNashorValue",
                              "type": "string"
                            }
                          },
                          "required": [
                            "name"
                          ],
                          "title": "LoLEventNashorObject",
                          "type": "object"
                        },
                        "type": {
                          "enum": [
                            "baron_nashor"
                          ],
                          "type": "string"
                        }
                      },
                      "required": [
                        "object",
                        "type"
                      ],
                      "title": "LoLEventNashor",
                      "type": "object"
                    },
                    {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "object": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
                            "champion": {
                              "additionalProperties": false,
                              "deprecated": false,
                              "properties": {
                                "id": {
                                  "minimum": 1,
                                  "title": "LoLChampionID",
                                  "type": "integer"
                                },
                                "name": {
                                  "title": "LoLChampionName",
                                  "type": "string"
                                }
                              },
                              "required": [
                                "id",
                                "name"
                              ],
                              "title": "LoLEventChampion",
                              "type": "object"
                            },
                            "player_id": {
                              "description": "ID of the player",
                              "minimum": 1,
                              "title": "PlayerID",
                              "type": "integer"
                            },
                            "player_name": {
                              "description": "Professional name of the player",
                              "title": "PlayerName",
                              "type": "string"
                            },
                            "side": {
                              "enum": [
                                "blue",
                                "red"
                              ],
                              "title": "LoLTeamColor",
                              "type": "string"
                            }
                          },
                          "required": [
                            "champion",
                            "player_id",
                            "player_name",
                            "side"
                          ],
                          "title": "LoLEventPlayerObject",
                          "type": "object"
                        },
                        "type": {
                          "enum": [
                            "player"
                          ],
                          "type": "string"
                        }
                      },
                      "required": [
                        "object",
                        "type"
                      ],
                      "title": "LoLEventPlayer",
                      "type": "object"
                    },
                    {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "object": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
                            "name": {
                              "enum": [
                                "Tower"
                              ],
                              "title": "LoLEventTowerValue",
                              "type": "string"
                            },
                            "side": {
                              "enum": [
                                "blue",
                                "red"
                              ],
                              "title": "LoLTeamColor",
                              "type": "string"
                            }
                          },
                          "required": [
                            "name",
                            "side"
                          ],
                          "title": "LoLEventTowerObject",
                          "type": "object"
                        },
                        "type": {
                          "enum": [
                            "tower"
                          ],
                          "type": "string"
                        }
                      },
                      "required": [
                        "object",
                        "type"
                      ],
                      "title": "LoLEventTower",
                      "type": "object"
                    },
                    {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "object": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
                            "name": {
                              "enum": [
                                "Big Corbin",
                                "Big Golem",
                                "Big Wolf",
                                "Blue Buff",
                                "Gromp",
                                "Red Buff",
                                "Small Corbin",
                                "Small Golem",
                                "Small Wolf"
                              ],
                              "title": "LoLEventNeutralMinionValue",
                              "type": "string"
                            }
                          },
                          "required": [
                            "name"
                          ],
                          "title": "LoLEventNeutralMinionObject",
                          "type": "object"
                        },
                        "type": {
                          "enum": [
                            "neutral_minion"
                          ],
                          "type": "string"
                        }
                      },
                      "required": [
                        "object",
                        "type"
                      ],
                      "title": "LoLEventNeutralMinion",
                      "type": "object"
                    },
                    {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "object": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
                            "name": {
                              "enum": [
                                "Voidgrub"
                              ],
                              "title": "LoLEventVoidgrubValue",
                              "type": "string"
                            }
                          },
                          "required": [
                            "name"
                          ],
                          "title": "LoLEventVoidgrubObject",
                          "type": "object"
                        },
                        "type": {
                          "enum": [
                            "voidgrub"
                          ],
                          "type": "string"
                        }
                      },
                      "required": [
                        "object",
                        "type"
                      ],
                      "title": "LoLEventVoidgrub",
                      "type": "object"
                    },
                    {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "object": {
                          "enum": [
                            null
                          ],
                          "nullable": true
                        },
                        "type": {
                          "enum": [
                            "unknown"
                          ],
                          "type": "string"
                        }
                      },
                      "required": [
                        "type"
                      ],
                      "title": "LoLEventUnknown",
                      "type": "object"
                    }
                  ],
                  "title": "LoLEventKiller"
                },
                "victim": {
                  "oneOf": [
                    {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "object": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
                            "name": {
                              "enum": [
                                "Atakhan"
                              ],
                              "title": "LoLEventAtakhanValue",
                              "type": "string"
                            }
                          },
                          "required": [
                            "name"
                          ],
                          "title": "LoLEventAtakhanObject",
                          "type": "object"
                        },
                        "type": {
                          "enum": [
                            "atakhan"
                          ],
                          "type": "string"
                        }
                      },
                      "required": [
                        "object",
                        "type"
                      ],
                      "title": "LoLEventAtakhan",
                      "type": "object"
                    },
                    {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "object": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
                            "name": {
                              "enum": [
                                "Chemtech Drake",
                                "Cloud Drake",
                                "Elder Drake",
                                "Hextech Drake",
                                "Infernal Drake",
                                "Mountain Drake",
                                "Ocean Drake"
                              ],
                              "title": "LoLDrakeName",
                              "type": "string"
                            },
                            "type": {
                              "enum": [
                                "chemtech",
                                "cloud",
                                "elder",
                                "hextech",
                                "infernal",
                                "mountain",
                                "ocean"
                              ],
                              "title": "LoLDrakeType",
                              "type": "string"
                            }
                          },
                          "required": [
                            "name",
                            "type"
                          ],
                          "title": "LoLEventDrakeObject",
                          "type": "object"
                        },
                        "type": {
                          "enum": [
                            "drake"
                          ],
                          "type": "string"
                        }
                      },
                      "required": [
                        "object",
                        "type"
                      ],
                      "title": "LoLEventDrake",
                      "type": "object"
                    },
                    {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "object": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
                            "name": {
                              "enum": [
                                "Rift Herald",
                                "riftherald"
                              ],
                              "title": "LoLEventHeraldValue",
                              "type": "string"
                            }
                          },
                          "required": [
                            "name"
                          ],
                          "title": "LoLEventHeraldObject",
                          "type": "object"
                        },
                        "type": {
                          "enum": [
                            "herald",
                            "rift_herald"
                          ],
                          "type": "string"
                        }
                      },
                      "required": [
                        "object",
                        "type"
                      ],
                      "title": "LoLEventHerald",
                      "type": "object"
                    },
                    {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "object": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
                            "name": {
                              "enum": [
                                "Baron Nashor"
                              ],
                              "title": "LoLEventNashorValue",
                              "type": "string"
                            }
                          },
                          "required": [
                            "name"
                          ],
                          "title": "LoLEventNashorObject",
                          "type": "object"
                        },
                        "type": {
                          "enum": [
                            "baron_nashor"
                          ],
                          "type": "string"
                        }
                      },
                      "required": [
                        "object",
                        "type"
                      ],
                      "title": "LoLEventNashor",
                      "type": "object"
                    },
                    {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "object": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
                            "champion": {
                              "additionalProperties": false,
                              "deprecated": false,
                              "properties": {
                                "id": {
                                  "minimum": 1,
                                  "title": "LoLChampionID",
                                  "type": "integer"
                                },
                                "name": {
                                  "title": "LoLChampionName",
                                  "type": "string"
                                }
                              },
                              "required": [
                                "id",
                                "name"
                              ],
                              "title": "LoLEventChampion",
                              "type": "object"
                            },
                            "player_id": {
                              "description": "ID of the player",
                              "minimum": 1,
                              "title": "PlayerID",
                              "type": "integer"
                            },
                            "player_name": {
                              "description": "Professional name of the player",
                              "title": "PlayerName",
                              "type": "string"
                            },
                            "side": {
                              "enum": [
                                "blue",
                                "red"
                              ],
                              "title": "LoLTeamColor",
                              "type": "string"
                            }
                          },
                          "required": [
                            "champion",
                            "player_id",
                            "player_name",
                            "side"
                          ],
                          "title": "LoLEventPlayerObject",
                          "type": "object"
                        },
                        "type": {
                          "enum": [
                            "player"
                          ],
                          "type": "string"
                        }
                      },
                      "required": [
                        "object",
                        "type"
                      ],
                      "title": "LoLEventPlayer",
                      "type": "object"
                    },
                    {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "object": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
                            "name": {
                              "enum": [
                                "Tower"
                              ],
                              "title": "LoLEventTowerValue",
                              "type": "string"
                            },
                            "side": {
                              "enum": [
                                "blue",
                                "red"
                              ],
                              "title": "LoLTeamColor",
                              "type": "string"
                            }
                          },
                          "required": [
                            "name",
                            "side"
                          ],
                          "title": "LoLEventTowerObject",
                          "type": "object"
                        },
                        "type": {
                          "enum": [
                            "tower"
                          ],
                          "type": "string"
                        }
                      },
                      "required": [
                        "object",
                        "type"
                      ],
                      "title": "LoLEventTower",
                      "type": "object"
                    },
                    {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "object": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
                            "name": {
                              "enum": [
                                "Inhibitor"
                              ],
                              "title": "LoLEventInhibitorValue",
                              "type": "string"
                            },
                            "side": {
                              "enum": [
                                "blue",
                                "red"
                              ],
                              "title": "LoLTeamColor",
                              "type": "string"
                            }
                          },
                          "required": [
                            "name",
                            "side"
                          ],
                          "title": "LoLEventInhibitorObject",
                          "type": "object"
                        },
                        "type": {
                          "enum": [
                            "inhibitor"
                          ],
                          "type": "string"
                        }
                      },
                      "required": [
                        "object",
                        "type"
                      ],
                      "title": "LoLEventInhibitor",
                      "type": "object"
                    },
                    {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "object": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
                            "name": {
                              "enum": [
                                "Voidgrub"
                              ],
                              "title": "LoLEventVoidgrubValue",
                              "type": "string"
                            }
                          },
                          "required": [
                            "name"
                          ],
                          "title": "LoLEventVoidgrubObject",
                          "type": "object"
                        },
                        "type": {
                          "enum": [
                            "voidgrub"
                          ],
                          "type": "string"
                        }
                      },
                      "required": [
                        "object",
                        "type"
                      ],
                      "title": "LoLEventVoidgrub",
                      "type": "object"
                    },
                    {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "object": {
                          "enum": [
                            null
                          ],
                          "nullable": true
                        },
                        "type": {
                          "enum": [
                            "unknown"
                          ],
                          "type": "string"
                        }
                      },
                      "required": [
                        "type"
                      ],
                      "title": "LoLEventUnknown",
                      "type": "object"
                    }
                  ],
                  "title": "LoLEventVictim"
                }
              },
              "required": [
                "assists",
                "killer",
                "victim"
              ],
              "title": "LoLEventPayload",
              "type": "object"
            },
            "tournament_id": {
              "minimum": 1,
              "title": "TournamentID",
              "type": "integer"
            },
            "type": {
              "enum": [
                "atakhan_kill",
                "baron_nashor_kill",
                "drake_kill",
                "inhibitor_kill",
                "other",
                "player_kill",
                "rift_herald_kill",
                "suicide",
                "tower_kill",
                "voidgrub_kill"
              ],
              "title": "LoLEventType",
              "type": "string"
            }
          },
          "required": [
            "game_id",
            "ingame_timestamp",
            "is_first",
            "match_id",
            "payload",
            "tournament_id",
            "type"
          ],
          "title": "LoLGameEvent",
          "type": "object"
        },
        "title": "LoLGameEvents",
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
    "/lol/games/{lol_game_id}/events": {
      "get": {
        "description": "List events for a given League of Legends game\n> ℹ️  \n> \n> This endpoint is only available to customers with a real-time data plan",
        "operationId": "get_lol_games_lolGameId_events",
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
            "$ref": "#/components/responses/LoLGameEvents"
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
        "summary": "List Play-by-Play events for a given game",
        "tags": [
          "LoL games"
        ],
        "x-pandascore-plan": "Basic real-time plan",
        "x-readme": {
          "code-samples": [
            {
              "code": "curl --request GET \\\n     --url 'https://api.pandascore.co/lol/games/{lol_game_id}/events' \\\n     --header 'accept: application/json'\n",
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