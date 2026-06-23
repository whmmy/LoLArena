> ## Documentation Index
> Fetch the complete documentation index at: https://developers.pandascore.co/llms.txt
> Use this file to discover all available pages before exploring further.

# List finished games for a given team

List finished games for a given League of Legends team
> ℹ️  
> 
> This endpoint is only available to customers with a historical or real-time data plan

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
      "LoLTeamLastGames": {
        "content": {
          "application/json": {
            "examples": {
              "/lol/teams/390/games?page[size]=1": {
                "description": "/lol/teams/390/games?page[size]=1",
                "value": [
                  {
                    "begin_at": "2025-08-30T21:51:10Z",
                    "complete": true,
                    "detailed_stats": true,
                    "end_at": "2025-08-30T22:36:09Z",
                    "finished": true,
                    "forfeit": false,
                    "id": 270073,
                    "length": 1995,
                    "match_id": 1209359,
                    "players": [
                      {
                        "assists": 5,
                        "champion": {
                          "id": 3740,
                          "image_url": "https://cdn.pandascore.co/images/lol/champion/image/d64af5dc-259e-4c06-94b8-4f60b0c47ff5.png",
                          "name": "Gangplank",
                          "slug": "Gangplank"
                        },
                        "creep_score": 235,
                        "cs_at_14": 90,
                        "cs_diff_at_14": 0,
                        "deaths": 6,
                        "flags": {
                          "first_blood_assist": true,
                          "first_blood_kill": false,
                          "first_inhibitor_assist": false,
                          "first_inhibitor_kill": false,
                          "first_tower_assist": false,
                          "first_tower_kill": false
                        },
                        "game_id": 270073,
                        "gold_earned": 14305,
                        "gold_percentage": 25.32,
                        "gold_spent": 14513,
                        "items": [
                          {
                            "id": 2446,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/0421f84dc8dd53dcb0e9d5a525145979.png",
                            "is_trinket": false,
                            "name": "Cloak of Agility"
                          },
                          {
                            "id": 2678,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                            "is_trinket": true,
                            "name": "Farsight Alteration"
                          },
                          {
                            "id": 3070,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/a5144a5e-4ba3-4400-bca8-6fbccc59e324.png",
                            "is_trinket": false,
                            "name": "Last Whisper"
                          },
                          {
                            "id": 3957,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/2b2a022c-de48-4503-a730-f0f57f2db24b.png",
                            "is_trinket": false,
                            "name": "Trinity Force"
                          },
                          {
                            "id": 4088,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/97a4459d-1008-4227-be87-10825e141897.png",
                            "is_trinket": false,
                            "name": "The Collector"
                          },
                          {
                            "id": 4205,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/c65c2df1-e666-492d-bf14-38e777163670.png",
                            "is_trinket": false,
                            "name": "Infinity Edge"
                          },
                          {
                            "id": 4206,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/d7bc469a-df47-420a-9c9e-f41a1cabf40b.png",
                            "is_trinket": false,
                            "name": "Mercury's Treads"
                          }
                        ],
                        "kills": 4,
                        "kills_counters": {
                          "inhibitors": 0,
                          "neutral_minions": 0,
                          "neutral_minions_enemy_jungle": 0,
                          "neutral_minions_team_jungle": 0,
                          "players": 4,
                          "turrets": 2,
                          "wards": 2
                        },
                        "kills_series": {
                          "double_kills": 0,
                          "penta_kills": 0,
                          "quadra_kills": 0,
                          "triple_kills": 0
                        },
                        "largest_critical_strike": 1203,
                        "largest_killing_spree": 0,
                        "largest_multi_kill": 1,
                        "level": 17,
                        "magic_damage": {
                          "dealt": 5107,
                          "dealt_percentage": 2.26,
                          "dealt_to_champions": 2987,
                          "dealt_to_champions_percentage": 6.98,
                          "taken": 8464
                        },
                        "masteries": [],
                        "minions_killed": 235,
                        "opponent": {
                          "acronym": "100",
                          "dark_mode_image_url": "https://cdn.pandascore.co/dark_images/team/dark_image/1537/190px_100_thieves_darkmode.png",
                          "id": 1537,
                          "image_url": "https://cdn.pandascore.co/images/team/image/1537/100_thieves_alternatelogo_square.png",
                          "location": "US",
                          "modified_at": "2025-09-24T08:57:45Z",
                          "name": "100 Thieves",
                          "slug": "100-thieves"
                        },
                        "physical_damage": {
                          "dealt": 195645,
                          "dealt_percentage": 39.58,
                          "dealt_to_champions": 16998,
                          "dealt_to_champions_percentage": 43.29,
                          "taken": 19762
                        },
                        "player": {
                          "active": true,
                          "age": 30,
                          "birthday": "1995-03-07",
                          "first_name": "Eon-yeong",
                          "id": 32,
                          "image_url": "https://cdn.pandascore.co/images/player/image/32/tl_impact_2025_split_1.png",
                          "last_name": "Jung",
                          "modified_at": "2025-09-24T14:31:31Z",
                          "name": "Impact",
                          "nationality": "KR",
                          "role": "top",
                          "slug": "impact"
                        },
                        "player_id": 32,
                        "role": "top",
                        "runes": [],
                        "runes_reforged": {
                          "primary_path": {
                            "id": 4,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/54c94cceac3bd8cf21be2a1e537a8880.png",
                            "keystone": {
                              "id": 40,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/5ccdfe9ed87cb8935b6a387a885410a8.png",
                              "name": "Grasp of the Undying",
                              "type": "keystone"
                            },
                            "lesser_runes": [
                              {
                                "id": 43,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/95b7572a3073bdf1640d7132365b01c8.png",
                                "name": "Demolish",
                                "type": "slot1"
                              },
                              {
                                "id": 47,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/3734b985fdb6c75e91ec7e0b92034869.png",
                                "name": "Second Wind",
                                "type": "slot2"
                              },
                              {
                                "id": 51,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/f6d5a0635d6ffa966708963cc4e1afc7.png",
                                "name": "Unflinching",
                                "type": "slot3"
                              }
                            ],
                            "name": "Resolve",
                            "type": "path"
                          },
                          "secondary_path": {
                            "id": 2,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                            "lesser_runes": [
                              {
                                "id": 23,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/1194b748d247fd494e848490df06e439.png",
                                "name": "Biscuit Delivery",
                                "type": "slot2"
                              },
                              {
                                "id": 24,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                                "name": "Cosmic Insight",
                                "type": "slot3"
                              }
                            ],
                            "name": "Inspiration",
                            "type": "path"
                          },
                          "shards": {
                            "defense": {
                              "id": 72,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/82ecde52-ce41-4d3f-9e2c-f8fa940376a5.png",
                              "name": "Health",
                              "type": "shard"
                            },
                            "flex": {
                              "id": 71,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                              "name": "Adaptative Force",
                              "type": "shard"
                            },
                            "offense": {
                              "id": 71,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                              "name": "Adaptative Force",
                              "type": "shard"
                            }
                          }
                        },
                        "spells": [
                          {
                            "id": 134,
                            "image_url": "https://cdn.pandascore.co/images/lol/spell/image/7daefb32-5286-4b7a-83d5-b1ced1000769.png",
                            "name": "Flash"
                          },
                          {
                            "id": 139,
                            "image_url": "https://cdn.pandascore.co/images/lol/spell/image/8a267861-63a9-4867-bfc2-3f2e06c11445.png",
                            "name": "Teleport"
                          }
                        ],
                        "team": {
                          "acronym": "TL",
                          "dark_mode_image_url": "https://cdn.pandascore.co/dark_images/team/dark_image/390/463px_team_liquid_2024_full_darkmode.png",
                          "id": 390,
                          "image_url": "https://cdn.pandascore.co/images/team/image/390/463px_team_liquid_2024_full_lightmode.png",
                          "location": "NL",
                          "modified_at": "2025-09-24T14:31:31Z",
                          "name": "Team Liquid",
                          "slug": "liquid"
                        },
                        "total_damage": {
                          "dealt": 213977,
                          "dealt_percentage": 25.97,
                          "dealt_to_champions": 24090,
                          "dealt_to_champions_percentage": 26.98,
                          "taken": 29848
                        },
                        "total_heal": 5281,
                        "total_time_crowd_control_dealt": 301,
                        "total_units_healed": 1,
                        "true_damage": {
                          "dealt": 13223,
                          "dealt_percentage": 12.71,
                          "dealt_to_champions": 4104,
                          "dealt_to_champions_percentage": 57.01,
                          "taken": 1621
                        },
                        "wards": {
                          "placed": 17,
                          "sight_wards_bought_in_game": 0,
                          "vision_wards_bought_in_game": 4
                        },
                        "wards_placed": 17
                      },
                      {
                        "assists": 7,
                        "champion": {
                          "id": 3602,
                          "image_url": "https://cdn.pandascore.co/images/lol/champion/image/7f3bc843-2a30-4e14-9cfa-0d8895d2dec4.png",
                          "name": "Nautilus",
                          "slug": "Nautilus"
                        },
                        "creep_score": 40,
                        "cs_at_14": 27,
                        "cs_diff_at_14": 9,
                        "deaths": 4,
                        "flags": {
                          "first_blood_assist": false,
                          "first_blood_kill": false,
                          "first_inhibitor_assist": false,
                          "first_inhibitor_kill": false,
                          "first_tower_assist": false,
                          "first_tower_kill": false
                        },
                        "game_id": 270073,
                        "gold_earned": 7233,
                        "gold_percentage": 12.8,
                        "gold_spent": 6925,
                        "items": [
                          {
                            "id": 2450,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/5ff4236356a2fc30dd646724b53a5354.png",
                            "is_trinket": false,
                            "name": "Cloth Armor"
                          },
                          {
                            "id": 2474,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                            "is_trinket": false,
                            "name": "Control Ward"
                          },
                          {
                            "id": 2679,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                            "is_trinket": true,
                            "name": "Oracle Lens"
                          },
                          {
                            "id": 3357,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/512b5dc6-4bfc-4397-9d9c-26863c99a383.png",
                            "is_trinket": false,
                            "name": "Kindlegem"
                          },
                          {
                            "id": 3408,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/9c04572e-a4a7-459e-948c-c2a0e00fdc2d.png",
                            "is_trinket": false,
                            "name": "Celestial Opposition"
                          },
                          {
                            "id": 3991,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/b76c580c-a13d-4683-af69-6c2a714c7f78.png",
                            "is_trinket": false,
                            "name": "Mikael's Blessing"
                          },
                          {
                            "id": 4206,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/d7bc469a-df47-420a-9c9e-f41a1cabf40b.png",
                            "is_trinket": false,
                            "name": "Mercury's Treads"
                          }
                        ],
                        "kills": 0,
                        "kills_counters": {
                          "inhibitors": 0,
                          "neutral_minions": 0,
                          "neutral_minions_enemy_jungle": 0,
                          "neutral_minions_team_jungle": 0,
                          "players": 0,
                          "turrets": 0,
                          "wards": 8
                        },
                        "kills_series": {
                          "double_kills": 0,
                          "penta_kills": 0,
                          "quadra_kills": 0,
                          "triple_kills": 0
                        },
                        "largest_critical_strike": 0,
                        "largest_killing_spree": 0,
                        "largest_multi_kill": 0,
                        "level": 13,
                        "magic_damage": {
                          "dealt": 7272,
                          "dealt_percentage": 3.22,
                          "dealt_to_champions": 2674,
                          "dealt_to_champions_percentage": 6.24,
                          "taken": 7869
                        },
                        "masteries": [],
                        "minions_killed": 40,
                        "opponent": {
                          "acronym": "100",
                          "dark_mode_image_url": "https://cdn.pandascore.co/dark_images/team/dark_image/1537/190px_100_thieves_darkmode.png",
                          "id": 1537,
                          "image_url": "https://cdn.pandascore.co/images/team/image/1537/100_thieves_alternatelogo_square.png",
                          "location": "US",
                          "modified_at": "2025-09-24T08:57:45Z",
                          "name": "100 Thieves",
                          "slug": "100-thieves"
                        },
                        "physical_damage": {
                          "dealt": 5807,
                          "dealt_percentage": 1.17,
                          "dealt_to_champions": 972,
                          "dealt_to_champions_percentage": 2.48,
                          "taken": 12172
                        },
                        "player": {
                          "active": true,
                          "age": 31,
                          "birthday": "1994-06-22",
                          "first_name": "Jo",
                          "id": 47,
                          "image_url": "https://cdn.pandascore.co/images/player/image/47/tl_core_jj_2025_split_1.png",
                          "last_name": "Yong-in",
                          "modified_at": "2025-08-30T19:13:44Z",
                          "name": "CoreJJ",
                          "nationality": "KR",
                          "role": "sup",
                          "slug": "corejj"
                        },
                        "player_id": 47,
                        "role": "sup",
                        "runes": [],
                        "runes_reforged": {
                          "primary_path": {
                            "id": 2,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                            "keystone": {
                              "id": 16,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/a6c5c38e514d454a5f8b5ccd1dbc5a91.png",
                              "name": "Unsealed Spellbook",
                              "type": "keystone"
                            },
                            "lesser_runes": [
                              {
                                "id": 18,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/09d2bb0b95d08979f13568a57be5cc06.png",
                                "name": "Hextech Flashtraption",
                                "type": "slot1"
                              },
                              {
                                "id": 23,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/1194b748d247fd494e848490df06e439.png",
                                "name": "Biscuit Delivery",
                                "type": "slot2"
                              },
                              {
                                "id": 24,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                                "name": "Cosmic Insight",
                                "type": "slot3"
                              }
                            ],
                            "name": "Inspiration",
                            "type": "path"
                          },
                          "secondary_path": {
                            "id": 4,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/54c94cceac3bd8cf21be2a1e537a8880.png",
                            "lesser_runes": [
                              {
                                "id": 51,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/f6d5a0635d6ffa966708963cc4e1afc7.png",
                                "name": "Unflinching",
                                "type": "slot3"
                              },
                              {
                                "id": 47,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/3734b985fdb6c75e91ec7e0b92034869.png",
                                "name": "Second Wind",
                                "type": "slot2"
                              }
                            ],
                            "name": "Resolve",
                            "type": "path"
                          },
                          "shards": {
                            "defense": {
                              "id": 72,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/82ecde52-ce41-4d3f-9e2c-f8fa940376a5.png",
                              "name": "Health",
                              "type": "shard"
                            },
                            "flex": {
                              "id": 73,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/18f82b15-e05c-4c85-a0ea-9c8e6812b5de.png",
                              "name": "Move Speed",
                              "type": "shard"
                            },
                            "offense": {
                              "id": 69,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                              "name": "Attack Speed",
                              "type": "shard"
                            }
                          }
                        },
                        "spells": [
                          {
                            "id": 134,
                            "image_url": "https://cdn.pandascore.co/images/lol/spell/image/7daefb32-5286-4b7a-83d5-b1ced1000769.png",
                            "name": "Flash"
                          },
                          {
                            "id": 136,
                            "image_url": "https://cdn.pandascore.co/images/lol/spell/image/b507c483-4be5-43c5-8456-e49d11fd4078.png",
                            "name": "Heal"
                          }
                        ],
                        "team": {
                          "acronym": "TL",
                          "dark_mode_image_url": "https://cdn.pandascore.co/dark_images/team/dark_image/390/463px_team_liquid_2024_full_darkmode.png",
                          "id": 390,
                          "image_url": "https://cdn.pandascore.co/images/team/image/390/463px_team_liquid_2024_full_lightmode.png",
                          "location": "NL",
                          "modified_at": "2025-09-24T14:31:31Z",
                          "name": "Team Liquid",
                          "slug": "liquid"
                        },
                        "total_damage": {
                          "dealt": 16017,
                          "dealt_percentage": 1.94,
                          "dealt_to_champions": 3873,
                          "dealt_to_champions_percentage": 4.34,
                          "taken": 21214
                        },
                        "total_heal": 3727,
                        "total_time_crowd_control_dealt": 159,
                        "total_units_healed": 4,
                        "true_damage": {
                          "dealt": 2937,
                          "dealt_percentage": 2.82,
                          "dealt_to_champions": 226,
                          "dealt_to_champions_percentage": 3.14,
                          "taken": 1172
                        },
                        "wards": {
                          "placed": 63,
                          "sight_wards_bought_in_game": 0,
                          "vision_wards_bought_in_game": 18
                        },
                        "wards_placed": 63
                      },
                      {
                        "assists": 9,
                        "champion": {
                          "id": 3699,
                          "image_url": "https://cdn.pandascore.co/images/lol/champion/image/c9d3bba6-a40f-40bf-9f59-3dffd5f00df0.png",
                          "name": "Sivir",
                          "slug": "Sivir"
                        },
                        "creep_score": 295,
                        "cs_at_14": 112,
                        "cs_diff_at_14": -11,
                        "deaths": 3,
                        "flags": {
                          "first_blood_assist": false,
                          "first_blood_kill": false,
                          "first_inhibitor_assist": false,
                          "first_inhibitor_kill": false,
                          "first_tower_assist": false,
                          "first_tower_kill": false
                        },
                        "game_id": 270073,
                        "gold_earned": 15308,
                        "gold_percentage": 21.91,
                        "gold_spent": 14975,
                        "items": [
                          {
                            "id": 2678,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                            "is_trinket": true,
                            "name": "Farsight Alteration"
                          },
                          {
                            "id": 3894,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/c15f5773-31ad-41b2-9dc1-8d702fc84e04.png",
                            "is_trinket": false,
                            "name": "Doran's Blade"
                          },
                          {
                            "id": 4031,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/d7f83028-1869-48ba-8142-968839f882f1.png",
                            "is_trinket": false,
                            "name": "Navori Flickerblade"
                          },
                          {
                            "id": 4049,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/4d568c1d-461e-4b1b-9344-873886c48fe2.png",
                            "is_trinket": false,
                            "name": "Essence Reaver"
                          },
                          {
                            "id": 4144,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/f7d322e7-e0a3-4c8c-877d-72cc5e5ec5ae.png",
                            "is_trinket": false,
                            "name": "Lord Dominik's Regards"
                          },
                          {
                            "id": 4205,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/c65c2df1-e666-492d-bf14-38e777163670.png",
                            "is_trinket": false,
                            "name": "Infinity Edge"
                          },
                          {
                            "id": 4380,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/a80543a8-5917-44ca-9fd5-944612a87450.png",
                            "is_trinket": false,
                            "name": "Armored Advance"
                          }
                        ],
                        "kills": 3,
                        "kills_counters": {
                          "inhibitors": 0,
                          "neutral_minions": 15,
                          "neutral_minions_enemy_jungle": 5,
                          "neutral_minions_team_jungle": 9,
                          "players": 3,
                          "turrets": 2,
                          "wards": 9
                        },
                        "kills_series": {
                          "double_kills": 0,
                          "penta_kills": 0,
                          "quadra_kills": 0,
                          "triple_kills": 0
                        },
                        "largest_critical_strike": 763,
                        "largest_killing_spree": 2,
                        "largest_multi_kill": 1,
                        "level": 17,
                        "magic_damage": {
                          "dealt": 8,
                          "dealt_percentage": 0,
                          "dealt_to_champions": 0,
                          "dealt_to_champions_percentage": 0,
                          "taken": 5030
                        },
                        "masteries": [],
                        "minions_killed": 295,
                        "opponent": {
                          "acronym": "TL",
                          "dark_mode_image_url": "https://cdn.pandascore.co/dark_images/team/dark_image/390/463px_team_liquid_2024_full_darkmode.png",
                          "id": 390,
                          "image_url": "https://cdn.pandascore.co/images/team/image/390/463px_team_liquid_2024_full_lightmode.png",
                          "location": "NL",
                          "modified_at": "2025-09-24T14:31:31Z",
                          "name": "Team Liquid",
                          "slug": "liquid"
                        },
                        "physical_damage": {
                          "dealt": 229227,
                          "dealt_percentage": 41.69,
                          "dealt_to_champions": 21538,
                          "dealt_to_champions_percentage": 41.49,
                          "taken": 9012
                        },
                        "player": {
                          "active": true,
                          "age": 26,
                          "birthday": "1999-02-11",
                          "first_name": "Victor",
                          "id": 1612,
                          "image_url": "https://cdn.pandascore.co/images/player/image/1612/100_t_fbi_2025_split_3.png",
                          "last_name": "Huang",
                          "modified_at": "2025-09-24T08:57:45Z",
                          "name": "FBI",
                          "nationality": "AU",
                          "role": "adc",
                          "slug": "fbi"
                        },
                        "player_id": 1612,
                        "role": "adc",
                        "runes": [],
                        "runes_reforged": {
                          "primary_path": {
                            "id": 3,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                            "keystone": {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/d11f16420cc7a65ce1f1253d0adf5459.png",
                              "name": "Lethal Tempo",
                              "type": "keystone"
                            },
                            "lesser_runes": [
                              {
                                "id": 33,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/63f58c2d747e2997472d1a3af2450e4e.png",
                                "name": "Presence of Mind",
                                "type": "slot1"
                              },
                              {
                                "id": 36,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/078fa7db48ed5384e9933f535f0b986a.png",
                                "name": "Legend: Bloodline",
                                "type": "slot2"
                              },
                              {
                                "id": 38,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/08f4edce2a6f85edbfea701c04314cb9.png",
                                "name": "Cut Down",
                                "type": "slot3"
                              }
                            ],
                            "name": "Precision",
                            "type": "path"
                          },
                          "secondary_path": {
                            "id": 2,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                            "lesser_runes": [
                              {
                                "id": 19,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/44b7c635b7abab80f429fc8d8bbf8718.png",
                                "name": "Magical Footwear",
                                "type": "slot1"
                              },
                              {
                                "id": 24,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                                "name": "Cosmic Insight",
                                "type": "slot3"
                              }
                            ],
                            "name": "Inspiration",
                            "type": "path"
                          },
                          "shards": {
                            "defense": {
                              "id": 72,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/82ecde52-ce41-4d3f-9e2c-f8fa940376a5.png",
                              "name": "Health",
                              "type": "shard"
                            },
                            "flex": {
                              "id": 71,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                              "name": "Adaptative Force",
                              "type": "shard"
                            },
                            "offense": {
                              "id": 69,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                              "name": "Attack Speed",
                              "type": "shard"
                            }
                          }
                        },
                        "spells": [
                          {
                            "id": 134,
                            "image_url": "https://cdn.pandascore.co/images/lol/spell/image/7daefb32-5286-4b7a-83d5-b1ced1000769.png",
                            "name": "Flash"
                          },
                          {
                            "id": 135,
                            "image_url": "https://cdn.pandascore.co/images/lol/spell/image/520c8a08-cc4b-4361-8662-c1f655784823.png",
                            "name": "Ghost"
                          }
                        ],
                        "team": {
                          "acronym": "100",
                          "dark_mode_image_url": "https://cdn.pandascore.co/dark_images/team/dark_image/1537/190px_100_thieves_darkmode.png",
                          "id": 1537,
                          "image_url": "https://cdn.pandascore.co/images/team/image/1537/100_thieves_alternatelogo_square.png",
                          "location": "US",
                          "modified_at": "2025-09-24T08:57:45Z",
                          "name": "100 Thieves",
                          "slug": "100-thieves"
                        },
                        "total_damage": {
                          "dealt": 232671,
                          "dealt_percentage": 23.06,
                          "dealt_to_champions": 22504,
                          "dealt_to_champions_percentage": 21.32,
                          "taken": 15326
                        },
                        "total_heal": 4792,
                        "total_time_crowd_control_dealt": 83,
                        "total_units_healed": 1,
                        "true_damage": {
                          "dealt": 3435,
                          "dealt_percentage": 2.9,
                          "dealt_to_champions": 965,
                          "dealt_to_champions_percentage": 10.61,
                          "taken": 1283
                        },
                        "wards": {
                          "placed": 15,
                          "sight_wards_bought_in_game": 0,
                          "vision_wards_bought_in_game": 5
                        },
                        "wards_placed": 15
                      },
                      {
                        "assists": 5,
                        "champion": {
                          "id": 3621,
                          "image_url": "https://cdn.pandascore.co/images/lol/champion/image/d945211d-bbc0-426a-b451-05bec64dee69.png",
                          "name": "Renekton",
                          "slug": "Renekton"
                        },
                        "creep_score": 257,
                        "cs_at_14": 90,
                        "cs_diff_at_14": 0,
                        "deaths": 3,
                        "flags": {
                          "first_blood_assist": false,
                          "first_blood_kill": false,
                          "first_inhibitor_assist": false,
                          "first_inhibitor_kill": false,
                          "first_tower_assist": false,
                          "first_tower_kill": false
                        },
                        "game_id": 270073,
                        "gold_earned": 15852,
                        "gold_percentage": 22.69,
                        "gold_spent": 12575,
                        "items": [
                          {
                            "id": 2449,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/6db62c8691e2f6f35efb0eff6e55df41.png",
                            "is_trinket": false,
                            "name": "Ruby Crystal"
                          },
                          {
                            "id": 2679,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                            "is_trinket": true,
                            "name": "Oracle Lens"
                          },
                          {
                            "id": 3621,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/6fcd6021-6611-427b-a176-0fa7244c1f6e.png",
                            "is_trinket": false,
                            "name": "Sterak's Gage"
                          },
                          {
                            "id": 3986,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/0e97c2ab-fa86-4741-aac0-c60354827bd9.png",
                            "is_trinket": false,
                            "name": "Spear of Shojin"
                          },
                          {
                            "id": 4015,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/87316979-992f-4138-b4e6-4123eb55035f.png",
                            "is_trinket": false,
                            "name": "Death's Dance"
                          },
                          {
                            "id": 4380,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/a80543a8-5917-44ca-9fd5-944612a87450.png",
                            "is_trinket": false,
                            "name": "Armored Advance"
                          }
                        ],
                        "kills": 8,
                        "kills_counters": {
                          "inhibitors": 0,
                          "neutral_minions": 0,
                          "neutral_minions_enemy_jungle": 0,
                          "neutral_minions_team_jungle": 0,
                          "players": 8,
                          "turrets": 4,
                          "wards": 14
                        },
                        "kills_series": {
                          "double_kills": 2,
                          "penta_kills": 0,
                          "quadra_kills": 0,
                          "triple_kills": 1
                        },
                        "largest_critical_strike": 0,
                        "largest_killing_spree": 6,
                        "largest_multi_kill": 3,
                        "level": 18,
                        "magic_damage": {
                          "dealt": 10738,
                          "dealt_percentage": 3.15,
                          "dealt_to_champions": 4683,
                          "dealt_to_champions_percentage": 10.51,
                          "taken": 15849
                        },
                        "masteries": [],
                        "minions_killed": 257,
                        "opponent": {
                          "acronym": "TL",
                          "dark_mode_image_url": "https://cdn.pandascore.co/dark_images/team/dark_image/390/463px_team_liquid_2024_full_darkmode.png",
                          "id": 390,
                          "image_url": "https://cdn.pandascore.co/images/team/image/390/463px_team_liquid_2024_full_lightmode.png",
                          "location": "NL",
                          "modified_at": "2025-09-24T14:31:31Z",
                          "name": "Team Liquid",
                          "slug": "liquid"
                        },
                        "physical_damage": {
                          "dealt": 173611,
                          "dealt_percentage": 31.57,
                          "dealt_to_champions": 17768,
                          "dealt_to_champions_percentage": 34.23,
                          "taken": 14276
                        },
                        "player": {
                          "active": true,
                          "age": 28,
                          "birthday": "1997-07-17",
                          "first_name": "Niship",
                          "id": 3468,
                          "image_url": "https://cdn.pandascore.co/images/player/image/3468/ezgif_5_4f27ddb481.png",
                          "last_name": "Doshi",
                          "modified_at": "2025-09-24T08:57:45Z",
                          "name": "Dhokla",
                          "nationality": "US",
                          "role": "top",
                          "slug": "dhokla"
                        },
                        "player_id": 3468,
                        "role": "top",
                        "runes": [],
                        "runes_reforged": {
                          "primary_path": {
                            "id": 3,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                            "keystone": {
                              "id": 30,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/aefc7bda4b2d6549ef850c58a9888a9a.png",
                              "name": "Conqueror",
                              "type": "keystone"
                            },
                            "lesser_runes": [
                              {
                                "id": 32,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/f84c3f1382361720c8acf85febfd7461.png",
                                "name": "Triumph",
                                "type": "slot1"
                              },
                              {
                                "id": 34,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/acbf363d31d30086d5f27ac65439f145.png",
                                "name": "Legend: Alacrity",
                                "type": "slot2"
                              },
                              {
                                "id": 39,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/726099ed11eed3e8515e702abd2bbf2a.png",
                                "name": "Last Stand",
                                "type": "slot3"
                              }
                            ],
                            "name": "Precision",
                            "type": "path"
                          },
                          "secondary_path": {
                            "id": 4,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/54c94cceac3bd8cf21be2a1e537a8880.png",
                            "lesser_runes": [
                              {
                                "id": 51,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/f6d5a0635d6ffa966708963cc4e1afc7.png",
                                "name": "Unflinching",
                                "type": "slot3"
                              },
                              {
                                "id": 47,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/3734b985fdb6c75e91ec7e0b92034869.png",
                                "name": "Second Wind",
                                "type": "slot2"
                              }
                            ],
                            "name": "Resolve",
                            "type": "path"
                          },
                          "shards": {
                            "defense": {
                              "id": 72,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/82ecde52-ce41-4d3f-9e2c-f8fa940376a5.png",
                              "name": "Health",
                              "type": "shard"
                            },
                            "flex": {
                              "id": 71,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                              "name": "Adaptative Force",
                              "type": "shard"
                            },
                            "offense": {
                              "id": 71,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                              "name": "Adaptative Force",
                              "type": "shard"
                            }
                          }
                        },
                        "spells": [
                          {
                            "id": 134,
                            "image_url": "https://cdn.pandascore.co/images/lol/spell/image/7daefb32-5286-4b7a-83d5-b1ced1000769.png",
                            "name": "Flash"
                          },
                          {
                            "id": 139,
                            "image_url": "https://cdn.pandascore.co/images/lol/spell/image/8a267861-63a9-4867-bfc2-3f2e06c11445.png",
                            "name": "Teleport"
                          }
                        ],
                        "team": {
                          "acronym": "100",
                          "dark_mode_image_url": "https://cdn.pandascore.co/dark_images/team/dark_image/1537/190px_100_thieves_darkmode.png",
                          "id": 1537,
                          "image_url": "https://cdn.pandascore.co/images/team/image/1537/100_thieves_alternatelogo_square.png",
                          "location": "US",
                          "modified_at": "2025-09-24T08:57:45Z",
                          "name": "100 Thieves",
                          "slug": "100-thieves"
                        },
                        "total_damage": {
                          "dealt": 189227,
                          "dealt_percentage": 18.75,
                          "dealt_to_champions": 22869,
                          "dealt_to_champions_percentage": 21.67,
                          "taken": 34947
                        },
                        "total_heal": 11419,
                        "total_time_crowd_control_dealt": 98,
                        "total_units_healed": 1,
                        "true_damage": {
                          "dealt": 4876,
                          "dealt_percentage": 4.11,
                          "dealt_to_champions": 418,
                          "dealt_to_champions_percentage": 4.6,
                          "taken": 4821
                        },
                        "wards": {
                          "placed": 9,
                          "sight_wards_bought_in_game": 0,
                          "vision_wards_bought_in_game": 3
                        },
                        "wards_placed": 9
                      },
                      {
                        "assists": 15,
                        "champion": {
                          "id": 3620,
                          "image_url": "https://cdn.pandascore.co/images/lol/champion/image/dfb6c9f0-de96-4af1-a7dd-06c054106459.png",
                          "name": "Renata Glasc",
                          "slug": "Renata"
                        },
                        "creep_score": 39,
                        "cs_at_14": 18,
                        "cs_diff_at_14": -9,
                        "deaths": 2,
                        "flags": {
                          "first_blood_assist": false,
                          "first_blood_kill": false,
                          "first_inhibitor_assist": true,
                          "first_inhibitor_kill": false,
                          "first_tower_assist": false,
                          "first_tower_kill": false
                        },
                        "game_id": 270073,
                        "gold_earned": 10084,
                        "gold_percentage": 14.44,
                        "gold_spent": 7700,
                        "items": [
                          {
                            "id": 2679,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                            "is_trinket": true,
                            "name": "Oracle Lens"
                          },
                          {
                            "id": 3357,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/512b5dc6-4bfc-4397-9d9c-26863c99a383.png",
                            "is_trinket": false,
                            "name": "Kindlegem"
                          },
                          {
                            "id": 3391,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/5f4d6b78-e7e8-4145-9d54-4dad34e319b7.png",
                            "is_trinket": false,
                            "name": "Ionian Boots of Lucidity"
                          },
                          {
                            "id": 3408,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/9c04572e-a4a7-459e-948c-c2a0e00fdc2d.png",
                            "is_trinket": false,
                            "name": "Celestial Opposition"
                          },
                          {
                            "id": 3967,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/580242b8-34c2-4333-bfa5-5b083335197a.png",
                            "is_trinket": false,
                            "name": "Redemption"
                          },
                          {
                            "id": 3991,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/b76c580c-a13d-4683-af69-6c2a714c7f78.png",
                            "is_trinket": false,
                            "name": "Mikael's Blessing"
                          }
                        ],
                        "kills": 3,
                        "kills_counters": {
                          "inhibitors": 0,
                          "neutral_minions": 0,
                          "neutral_minions_enemy_jungle": 0,
                          "neutral_minions_team_jungle": 0,
                          "players": 3,
                          "turrets": 1,
                          "wards": 24
                        },
                        "kills_series": {
                          "double_kills": 0,
                          "penta_kills": 0,
                          "quadra_kills": 0,
                          "triple_kills": 0
                        },
                        "largest_critical_strike": 85,
                        "largest_killing_spree": 2,
                        "largest_multi_kill": 1,
                        "level": 14,
                        "magic_damage": {
                          "dealt": 17548,
                          "dealt_percentage": 5.15,
                          "dealt_to_champions": 4058,
                          "dealt_to_champions_percentage": 9.11,
                          "taken": 3421
                        },
                        "masteries": [],
                        "minions_killed": 39,
                        "opponent": {
                          "acronym": "TL",
                          "dark_mode_image_url": "https://cdn.pandascore.co/dark_images/team/dark_image/390/463px_team_liquid_2024_full_darkmode.png",
                          "id": 390,
                          "image_url": "https://cdn.pandascore.co/images/team/image/390/463px_team_liquid_2024_full_lightmode.png",
                          "location": "NL",
                          "modified_at": "2025-09-24T14:31:31Z",
                          "name": "Team Liquid",
                          "slug": "liquid"
                        },
                        "physical_damage": {
                          "dealt": 5337,
                          "dealt_percentage": 0.97,
                          "dealt_to_champions": 1349,
                          "dealt_to_champions_percentage": 2.6,
                          "taken": 6234
                        },
                        "player": {
                          "active": true,
                          "age": 26,
                          "birthday": "1999-08-24",
                          "first_name": "Bill",
                          "id": 18026,
                          "image_url": "https://cdn.pandascore.co/images/player/image/18026/100_t_eyla_2025_split_3.png",
                          "last_name": "Nguyen",
                          "modified_at": "2025-09-24T08:57:45Z",
                          "name": "Eyla",
                          "nationality": "AU",
                          "role": "sup",
                          "slug": "eyla"
                        },
                        "player_id": 18026,
                        "role": "sup",
                        "runes": [],
                        "runes_reforged": {
                          "primary_path": {
                            "id": 2,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                            "keystone": {
                              "id": 16,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/a6c5c38e514d454a5f8b5ccd1dbc5a91.png",
                              "name": "Unsealed Spellbook",
                              "type": "keystone"
                            },
                            "lesser_runes": [
                              {
                                "id": 19,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/44b7c635b7abab80f429fc8d8bbf8718.png",
                                "name": "Magical Footwear",
                                "type": "slot1"
                              },
                              {
                                "id": 23,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/1194b748d247fd494e848490df06e439.png",
                                "name": "Biscuit Delivery",
                                "type": "slot2"
                              },
                              {
                                "id": 24,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                                "name": "Cosmic Insight",
                                "type": "slot3"
                              }
                            ],
                            "name": "Inspiration",
                            "type": "path"
                          },
                          "secondary_path": {
                            "id": 4,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/54c94cceac3bd8cf21be2a1e537a8880.png",
                            "lesser_runes": [
                              {
                                "id": 48,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/6054dc49089750c7d576b8e157228f29.png",
                                "name": "Bone Plating",
                                "type": "slot2"
                              },
                              {
                                "id": 51,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/f6d5a0635d6ffa966708963cc4e1afc7.png",
                                "name": "Unflinching",
                                "type": "slot3"
                              }
                            ],
                            "name": "Resolve",
                            "type": "path"
                          },
                          "shards": {
                            "defense": {
                              "id": 72,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/82ecde52-ce41-4d3f-9e2c-f8fa940376a5.png",
                              "name": "Health",
                              "type": "shard"
                            },
                            "flex": {
                              "id": 73,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/18f82b15-e05c-4c85-a0ea-9c8e6812b5de.png",
                              "name": "Move Speed",
                              "type": "shard"
                            },
                            "offense": {
                              "id": 69,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                              "name": "Attack Speed",
                              "type": "shard"
                            }
                          }
                        },
                        "spells": [
                          {
                            "id": 134,
                            "image_url": "https://cdn.pandascore.co/images/lol/spell/image/7daefb32-5286-4b7a-83d5-b1ced1000769.png",
                            "name": "Flash"
                          },
                          {
                            "id": 136,
                            "image_url": "https://cdn.pandascore.co/images/lol/spell/image/b507c483-4be5-43c5-8456-e49d11fd4078.png",
                            "name": "Heal"
                          }
                        ],
                        "team": {
                          "acronym": "100",
                          "dark_mode_image_url": "https://cdn.pandascore.co/dark_images/team/dark_image/1537/190px_100_thieves_darkmode.png",
                          "id": 1537,
                          "image_url": "https://cdn.pandascore.co/images/team/image/1537/100_thieves_alternatelogo_square.png",
                          "location": "US",
                          "modified_at": "2025-09-24T08:57:45Z",
                          "name": "100 Thieves",
                          "slug": "100-thieves"
                        },
                        "total_damage": {
                          "dealt": 28193,
                          "dealt_percentage": 2.79,
                          "dealt_to_champions": 9545,
                          "dealt_to_champions_percentage": 9.04,
                          "taken": 12169
                        },
                        "total_heal": 7460,
                        "total_time_crowd_control_dealt": 167,
                        "total_units_healed": 10,
                        "true_damage": {
                          "dealt": 5307,
                          "dealt_percentage": 4.48,
                          "dealt_to_champions": 4136,
                          "dealt_to_champions_percentage": 45.48,
                          "taken": 2513
                        },
                        "wards": {
                          "placed": 59,
                          "sight_wards_bought_in_game": 0,
                          "vision_wards_bought_in_game": 16
                        },
                        "wards_placed": 59
                      },
                      {
                        "assists": 10,
                        "champion": {
                          "id": 3627,
                          "image_url": "https://cdn.pandascore.co/images/lol/champion/image/a75129ec-6f20-4cf4-b6d2-762fa64ad0a7.png",
                          "name": "Sejuani",
                          "slug": "Sejuani"
                        },
                        "creep_score": 225,
                        "cs_at_14": 100,
                        "cs_diff_at_14": 5,
                        "deaths": 2,
                        "flags": {
                          "first_blood_assist": false,
                          "first_blood_kill": false,
                          "first_inhibitor_assist": true,
                          "first_inhibitor_kill": false,
                          "first_tower_assist": false,
                          "first_tower_kill": true
                        },
                        "game_id": 270073,
                        "gold_earned": 12977,
                        "gold_percentage": 18.58,
                        "gold_spent": 9925,
                        "items": [
                          {
                            "id": 2445,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/5d76fb8969392486363994c43a0abc2d.png",
                            "is_trinket": false,
                            "name": "Giant's Belt"
                          },
                          {
                            "id": 2445,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/5d76fb8969392486363994c43a0abc2d.png",
                            "is_trinket": false,
                            "name": "Giant's Belt"
                          },
                          {
                            "id": 2679,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                            "is_trinket": true,
                            "name": "Oracle Lens"
                          },
                          {
                            "id": 3958,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/550c7154-25ba-4118-87b0-66699cf736c9.png",
                            "is_trinket": false,
                            "name": "Heartsteel"
                          },
                          {
                            "id": 3970,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/c35bff91-c607-4acc-97dc-4e4770b8bda4.png",
                            "is_trinket": false,
                            "name": "Frozen Heart"
                          },
                          {
                            "id": 4379,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/d8ec2fd4-b5d8-4611-a9df-81d2b2602922.png",
                            "is_trinket": false,
                            "name": "Chainlaced Crushers"
                          }
                        ],
                        "kills": 5,
                        "kills_counters": {
                          "inhibitors": 0,
                          "neutral_minions": 190,
                          "neutral_minions_enemy_jungle": 12,
                          "neutral_minions_team_jungle": 84,
                          "players": 5,
                          "turrets": 1,
                          "wards": 10
                        },
                        "kills_series": {
                          "double_kills": 0,
                          "penta_kills": 0,
                          "quadra_kills": 0,
                          "triple_kills": 0
                        },
                        "largest_critical_strike": 0,
                        "largest_killing_spree": 3,
                        "largest_multi_kill": 1,
                        "level": 17,
                        "magic_damage": {
                          "dealt": 51113,
                          "dealt_percentage": 15,
                          "dealt_to_champions": 5977,
                          "dealt_to_champions_percentage": 13.42,
                          "taken": 13880
                        },
                        "masteries": [],
                        "minions_killed": 225,
                        "opponent": {
                          "acronym": "TL",
                          "dark_mode_image_url": "https://cdn.pandascore.co/dark_images/team/dark_image/390/463px_team_liquid_2024_full_darkmode.png",
                          "id": 390,
                          "image_url": "https://cdn.pandascore.co/images/team/image/390/463px_team_liquid_2024_full_lightmode.png",
                          "location": "NL",
                          "modified_at": "2025-09-24T14:31:31Z",
                          "name": "Team Liquid",
                          "slug": "liquid"
                        },
                        "physical_damage": {
                          "dealt": 125644,
                          "dealt_percentage": 22.85,
                          "dealt_to_champions": 9765,
                          "dealt_to_champions_percentage": 18.81,
                          "taken": 22711
                        },
                        "player": {
                          "active": true,
                          "age": 26,
                          "birthday": "1999-07-23",
                          "first_name": "Kim",
                          "id": 18099,
                          "image_url": "https://cdn.pandascore.co/images/player/image/18099/100_t_river_2025_split_3.png",
                          "last_name": "Dong-woo",
                          "modified_at": "2025-09-24T08:57:45Z",
                          "name": "River",
                          "nationality": "KR",
                          "role": "jun",
                          "slug": "baby-a4193857-79e6-4f15-91cf-a510ab151fff"
                        },
                        "player_id": 18099,
                        "role": "jun",
                        "runes": [],
                        "runes_reforged": {
                          "primary_path": {
                            "id": 2,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                            "keystone": {
                              "id": 16,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/a6c5c38e514d454a5f8b5ccd1dbc5a91.png",
                              "name": "Unsealed Spellbook",
                              "type": "keystone"
                            },
                            "lesser_runes": [
                              {
                                "id": 19,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/44b7c635b7abab80f429fc8d8bbf8718.png",
                                "name": "Magical Footwear",
                                "type": "slot1"
                              },
                              {
                                "id": 76,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/8ff0a8d7-8977-45b2-a68e-47831c96c33b.png",
                                "name": "Triple Tonic",
                                "type": "slot2"
                              },
                              {
                                "id": 24,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                                "name": "Cosmic Insight",
                                "type": "slot3"
                              }
                            ],
                            "name": "Inspiration",
                            "type": "path"
                          },
                          "secondary_path": {
                            "id": 1,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/346a8dc90cb18766f2dfde90672a6118.png",
                            "lesser_runes": [
                              {
                                "id": 5,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/eea2c6cd75310f68cce8a704f37cf296.png",
                                "name": "Cheap Shot",
                                "type": "slot1"
                              },
                              {
                                "id": 14,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/c9305f3dcdc9b6711f90df9e6e0c849c.png",
                                "name": "Ultimate Hunter",
                                "type": "slot3"
                              }
                            ],
                            "name": "Domination",
                            "type": "path"
                          },
                          "shards": {
                            "defense": {
                              "id": 72,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/82ecde52-ce41-4d3f-9e2c-f8fa940376a5.png",
                              "name": "Health",
                              "type": "shard"
                            },
                            "flex": {
                              "id": 71,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                              "name": "Adaptative Force",
                              "type": "shard"
                            },
                            "offense": {
                              "id": 69,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                              "name": "Attack Speed",
                              "type": "shard"
                            }
                          }
                        },
                        "spells": [
                          {
                            "id": 134,
                            "image_url": "https://cdn.pandascore.co/images/lol/spell/image/7daefb32-5286-4b7a-83d5-b1ced1000769.png",
                            "name": "Flash"
                          },
                          {
                            "id": 138,
                            "image_url": "https://cdn.pandascore.co/images/lol/spell/image/ad094a10-953f-438b-a330-06978486c9bb.png",
                            "name": "Smite"
                          }
                        ],
                        "team": {
                          "acronym": "100",
                          "dark_mode_image_url": "https://cdn.pandascore.co/dark_images/team/dark_image/1537/190px_100_thieves_darkmode.png",
                          "id": 1537,
                          "image_url": "https://cdn.pandascore.co/images/team/image/1537/100_thieves_alternatelogo_square.png",
                          "location": "US",
                          "modified_at": "2025-09-24T08:57:45Z",
                          "name": "100 Thieves",
                          "slug": "100-thieves"
                        },
                        "total_damage": {
                          "dealt": 278232,
                          "dealt_percentage": 27.57,
                          "dealt_to_champions": 17300,
                          "dealt_to_champions_percentage": 16.39,
                          "taken": 37101
                        },
                        "total_heal": 17604,
                        "total_time_crowd_control_dealt": 603,
                        "total_units_healed": 1,
                        "true_damage": {
                          "dealt": 101474,
                          "dealt_percentage": 85.59,
                          "dealt_to_champions": 1557,
                          "dealt_to_champions_percentage": 17.12,
                          "taken": 509
                        },
                        "wards": {
                          "placed": 14,
                          "sight_wards_bought_in_game": 0,
                          "vision_wards_bought_in_game": 9
                        },
                        "wards_placed": 14
                      },
                      {
                        "assists": 4,
                        "champion": {
                          "id": 3777,
                          "image_url": "https://cdn.pandascore.co/images/lol/champion/image/e189f940-062a-4d14-bc94-04a126bc30bc.png",
                          "name": "Varus",
                          "slug": "Varus"
                        },
                        "creep_score": 266,
                        "cs_at_14": 123,
                        "cs_diff_at_14": 11,
                        "deaths": 5,
                        "flags": {
                          "first_blood_assist": false,
                          "first_blood_kill": false,
                          "first_inhibitor_assist": false,
                          "first_inhibitor_kill": false,
                          "first_tower_assist": false,
                          "first_tower_kill": false
                        },
                        "game_id": 270073,
                        "gold_earned": 11717,
                        "gold_percentage": 20.74,
                        "gold_spent": 11405,
                        "items": [
                          {
                            "id": 2474,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                            "is_trinket": false,
                            "name": "Control Ward"
                          },
                          {
                            "id": 2678,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                            "is_trinket": true,
                            "name": "Farsight Alteration"
                          },
                          {
                            "id": 3389,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/799f0935-b5d3-410e-8c1b-200a55ff38ad.png",
                            "is_trinket": false,
                            "name": "Blade of The Ruined King"
                          },
                          {
                            "id": 3941,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/7bd8d874-281a-416b-a85b-2f3c9801a233.png",
                            "is_trinket": false,
                            "name": "Berserker's Greaves"
                          },
                          {
                            "id": 3977,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/31854932-3c20-41e8-800b-70656cd04133.png",
                            "is_trinket": false,
                            "name": "Guinsoo's Rageblade"
                          },
                          {
                            "id": 3992,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/016a0877-7c29-4cbb-88de-70f14c692e38.png",
                            "is_trinket": false,
                            "name": "Terminus"
                          }
                        ],
                        "kills": 1,
                        "kills_counters": {
                          "inhibitors": 0,
                          "neutral_minions": 0,
                          "neutral_minions_enemy_jungle": 0,
                          "neutral_minions_team_jungle": 0,
                          "players": 1,
                          "turrets": 0,
                          "wards": 13
                        },
                        "kills_series": {
                          "double_kills": 0,
                          "penta_kills": 0,
                          "quadra_kills": 0,
                          "triple_kills": 0
                        },
                        "largest_critical_strike": 0,
                        "largest_killing_spree": 0,
                        "largest_multi_kill": 1,
                        "level": 14,
                        "magic_damage": {
                          "dealt": 23471,
                          "dealt_percentage": 10.41,
                          "dealt_to_champions": 7128,
                          "dealt_to_champions_percentage": 16.65,
                          "taken": 6085
                        },
                        "masteries": [],
                        "minions_killed": 266,
                        "opponent": {
                          "acronym": "100",
                          "dark_mode_image_url": "https://cdn.pandascore.co/dark_images/team/dark_image/1537/190px_100_thieves_darkmode.png",
                          "id": 1537,
                          "image_url": "https://cdn.pandascore.co/images/team/image/1537/100_thieves_alternatelogo_square.png",
                          "location": "US",
                          "modified_at": "2025-09-24T08:57:45Z",
                          "name": "100 Thieves",
                          "slug": "100-thieves"
                        },
                        "physical_damage": {
                          "dealt": 124955,
                          "dealt_percentage": 25.28,
                          "dealt_to_champions": 11466,
                          "dealt_to_champions_percentage": 29.2,
                          "taken": 15128
                        },
                        "player": {
                          "active": true,
                          "age": 24,
                          "birthday": "2001-01-07",
                          "first_name": "Sean",
                          "id": 32065,
                          "image_url": "https://cdn.pandascore.co/images/player/image/32065/tl_yeon_2025_split_1.png",
                          "last_name": "Sung",
                          "modified_at": "2025-08-30T19:13:58Z",
                          "name": "Yeon",
                          "nationality": "US",
                          "role": "adc",
                          "slug": "yeon"
                        },
                        "player_id": 32065,
                        "role": "adc",
                        "runes": [],
                        "runes_reforged": {
                          "primary_path": {
                            "id": 3,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                            "keystone": {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/d11f16420cc7a65ce1f1253d0adf5459.png",
                              "name": "Lethal Tempo",
                              "type": "keystone"
                            },
                            "lesser_runes": [
                              {
                                "id": 33,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/63f58c2d747e2997472d1a3af2450e4e.png",
                                "name": "Presence of Mind",
                                "type": "slot1"
                              },
                              {
                                "id": 34,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/acbf363d31d30086d5f27ac65439f145.png",
                                "name": "Legend: Alacrity",
                                "type": "slot2"
                              },
                              {
                                "id": 38,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/08f4edce2a6f85edbfea701c04314cb9.png",
                                "name": "Cut Down",
                                "type": "slot3"
                              }
                            ],
                            "name": "Precision",
                            "type": "path"
                          },
                          "secondary_path": {
                            "id": 2,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                            "lesser_runes": [
                              {
                                "id": 24,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                                "name": "Cosmic Insight",
                                "type": "slot3"
                              },
                              {
                                "id": 23,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/1194b748d247fd494e848490df06e439.png",
                                "name": "Biscuit Delivery",
                                "type": "slot2"
                              }
                            ],
                            "name": "Inspiration",
                            "type": "path"
                          },
                          "shards": {
                            "defense": {
                              "id": 72,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/82ecde52-ce41-4d3f-9e2c-f8fa940376a5.png",
                              "name": "Health",
                              "type": "shard"
                            },
                            "flex": {
                              "id": 71,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                              "name": "Adaptative Force",
                              "type": "shard"
                            },
                            "offense": {
                              "id": 69,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                              "name": "Attack Speed",
                              "type": "shard"
                            }
                          }
                        },
                        "spells": [
                          {
                            "id": 130,
                            "image_url": "https://cdn.pandascore.co/images/lol/spell/image/70e5cf4d-bed2-40e2-96d5-03ab3f8c193c.png",
                            "name": "Cleanse"
                          },
                          {
                            "id": 134,
                            "image_url": "https://cdn.pandascore.co/images/lol/spell/image/7daefb32-5286-4b7a-83d5-b1ced1000769.png",
                            "name": "Flash"
                          }
                        ],
                        "team": {
                          "acronym": "TL",
                          "dark_mode_image_url": "https://cdn.pandascore.co/dark_images/team/dark_image/390/463px_team_liquid_2024_full_darkmode.png",
                          "id": 390,
                          "image_url": "https://cdn.pandascore.co/images/team/image/390/463px_team_liquid_2024_full_lightmode.png",
                          "location": "NL",
                          "modified_at": "2025-09-24T14:31:31Z",
                          "name": "Team Liquid",
                          "slug": "liquid"
                        },
                        "total_damage": {
                          "dealt": 152632,
                          "dealt_percentage": 18.53,
                          "dealt_to_champions": 19099,
                          "dealt_to_champions_percentage": 21.39,
                          "taken": 22041
                        },
                        "total_heal": 6336,
                        "total_time_crowd_control_dealt": 328,
                        "total_units_healed": 1,
                        "true_damage": {
                          "dealt": 4205,
                          "dealt_percentage": 4.04,
                          "dealt_to_champions": 505,
                          "dealt_to_champions_percentage": 7.01,
                          "taken": 827
                        },
                        "wards": {
                          "placed": 12,
                          "sight_wards_bought_in_game": 0,
                          "vision_wards_bought_in_game": 7
                        },
                        "wards_placed": 12
                      },
                      {
                        "assists": 4,
                        "champion": {
                          "id": 3776,
                          "image_url": "https://cdn.pandascore.co/images/lol/champion/image/3ef6891e-09ef-4a29-ab82-53eaae10d1d1.png",
                          "name": "Taliyah",
                          "slug": "Taliyah"
                        },
                        "creep_score": 250,
                        "cs_at_14": 114,
                        "cs_diff_at_14": -39,
                        "deaths": 6,
                        "flags": {
                          "first_blood_assist": false,
                          "first_blood_kill": true,
                          "first_inhibitor_assist": false,
                          "first_inhibitor_kill": false,
                          "first_tower_assist": false,
                          "first_tower_kill": false
                        },
                        "game_id": 270073,
                        "gold_earned": 13294,
                        "gold_percentage": 23.53,
                        "gold_spent": 13125,
                        "items": [
                          {
                            "id": 2678,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                            "is_trinket": true,
                            "name": "Farsight Alteration"
                          },
                          {
                            "id": 3305,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/b920e467-3294-4632-a463-393b881aba52.png",
                            "is_trinket": false,
                            "name": "Dark Seal"
                          },
                          {
                            "id": 3329,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/2574875e-a890-4b5e-b2fb-c13aaae6b1b7.png",
                            "is_trinket": false,
                            "name": "Amplifying Tome"
                          },
                          {
                            "id": 3391,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/5f4d6b78-e7e8-4145-9d54-4dad34e319b7.png",
                            "is_trinket": false,
                            "name": "Ionian Boots of Lucidity"
                          },
                          {
                            "id": 3872,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/32088681-b7fc-4cfc-bbf9-fd574b3d4b31.png",
                            "is_trinket": false,
                            "name": "Void Staff"
                          },
                          {
                            "id": 3948,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/43be86c8-4a8a-4d54-9cbc-d06045cf8f7a.png",
                            "is_trinket": false,
                            "name": "Seraph's Embrace"
                          },
                          {
                            "id": 4013,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/e3d4e9b3-f7de-4be8-be41-5c8a851113cf.png",
                            "is_trinket": false,
                            "name": "Shadowflame"
                          }
                        ],
                        "kills": 6,
                        "kills_counters": {
                          "inhibitors": 0,
                          "neutral_minions": 8,
                          "neutral_minions_enemy_jungle": 0,
                          "neutral_minions_team_jungle": 2,
                          "players": 6,
                          "turrets": 0,
                          "wards": 9
                        },
                        "kills_series": {
                          "double_kills": 0,
                          "penta_kills": 0,
                          "quadra_kills": 0,
                          "triple_kills": 0
                        },
                        "largest_critical_strike": 0,
                        "largest_killing_spree": 4,
                        "largest_multi_kill": 1,
                        "level": 15,
                        "magic_damage": {
                          "dealt": 185386,
                          "dealt_percentage": 82.19,
                          "dealt_to_champions": 29400,
                          "dealt_to_champions_percentage": 68.66,
                          "taken": 7841
                        },
                        "masteries": [],
                        "minions_killed": 250,
                        "opponent": {
                          "acronym": "100",
                          "dark_mode_image_url": "https://cdn.pandascore.co/dark_images/team/dark_image/1537/190px_100_thieves_darkmode.png",
                          "id": 1537,
                          "image_url": "https://cdn.pandascore.co/images/team/image/1537/100_thieves_alternatelogo_square.png",
                          "location": "US",
                          "modified_at": "2025-09-24T08:57:45Z",
                          "name": "100 Thieves",
                          "slug": "100-thieves"
                        },
                        "physical_damage": {
                          "dealt": 9679,
                          "dealt_percentage": 1.96,
                          "dealt_to_champions": 1327,
                          "dealt_to_champions_percentage": 3.38,
                          "taken": 10832
                        },
                        "player": {
                          "active": true,
                          "age": 23,
                          "birthday": "2002-03-05",
                          "first_name": "Eain",
                          "id": 33658,
                          "image_url": "https://cdn.pandascore.co/images/player/image/33658/tl_apa_2025_split_1.png",
                          "last_name": "Stearns",
                          "modified_at": "2025-08-30T19:14:07Z",
                          "name": "APA",
                          "nationality": "US",
                          "role": "mid",
                          "slug": "apa"
                        },
                        "player_id": 33658,
                        "role": "mid",
                        "runes": [],
                        "runes_reforged": {
                          "primary_path": {
                            "id": 5,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/fedb6f0ca24988f397ad65670e1f9f76.png",
                            "keystone": {
                              "id": 54,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/4ee4739ae4a9cbf7be59650f92009edc.png",
                              "name": "Phase Rush",
                              "type": "keystone"
                            },
                            "lesser_runes": [
                              {
                                "id": 56,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/ce8144471d3d5b3ab7b13ceede28480f.png",
                                "name": "Manaflow Band",
                                "type": "slot1"
                              },
                              {
                                "id": 60,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/0103e35a695d637b86f7d6344653009b.png",
                                "name": "Absolute Focus",
                                "type": "slot2"
                              },
                              {
                                "id": 61,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/c34c227ecf5a2cb963ecde2005474d29.png",
                                "name": "Scorch",
                                "type": "slot3"
                              }
                            ],
                            "name": "Sorcery",
                            "type": "path"
                          },
                          "secondary_path": {
                            "id": 3,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                            "lesser_runes": [
                              {
                                "id": 79,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/1aee7893-608a-4293-b086-51b9fe3d0073.png",
                                "name": "Legend: Haste",
                                "type": "slot2"
                              },
                              {
                                "id": 38,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/08f4edce2a6f85edbfea701c04314cb9.png",
                                "name": "Cut Down",
                                "type": "slot3"
                              }
                            ],
                            "name": "Precision",
                            "type": "path"
                          },
                          "shards": {
                            "defense": {
                              "id": 72,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/82ecde52-ce41-4d3f-9e2c-f8fa940376a5.png",
                              "name": "Health",
                              "type": "shard"
                            },
                            "flex": {
                              "id": 71,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                              "name": "Adaptative Force",
                              "type": "shard"
                            },
                            "offense": {
                              "id": 69,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                              "name": "Attack Speed",
                              "type": "shard"
                            }
                          }
                        },
                        "spells": [
                          {
                            "id": 134,
                            "image_url": "https://cdn.pandascore.co/images/lol/spell/image/7daefb32-5286-4b7a-83d5-b1ced1000769.png",
                            "name": "Flash"
                          },
                          {
                            "id": 139,
                            "image_url": "https://cdn.pandascore.co/images/lol/spell/image/8a267861-63a9-4867-bfc2-3f2e06c11445.png",
                            "name": "Teleport"
                          }
                        ],
                        "team": {
                          "acronym": "TL",
                          "dark_mode_image_url": "https://cdn.pandascore.co/dark_images/team/dark_image/390/463px_team_liquid_2024_full_darkmode.png",
                          "id": 390,
                          "image_url": "https://cdn.pandascore.co/images/team/image/390/463px_team_liquid_2024_full_lightmode.png",
                          "location": "NL",
                          "modified_at": "2025-09-24T14:31:31Z",
                          "name": "Team Liquid",
                          "slug": "liquid"
                        },
                        "total_damage": {
                          "dealt": 197027,
                          "dealt_percentage": 23.91,
                          "dealt_to_champions": 32471,
                          "dealt_to_champions_percentage": 36.37,
                          "taken": 19332
                        },
                        "total_heal": 1997,
                        "total_time_crowd_control_dealt": 605,
                        "total_units_healed": 1,
                        "true_damage": {
                          "dealt": 1960,
                          "dealt_percentage": 1.88,
                          "dealt_to_champions": 1744,
                          "dealt_to_champions_percentage": 24.23,
                          "taken": 658
                        },
                        "wards": {
                          "placed": 22,
                          "sight_wards_bought_in_game": 0,
                          "vision_wards_bought_in_game": 11
                        },
                        "wards_placed": 22
                      },
                      {
                        "assists": 10,
                        "champion": {
                          "id": 3625,
                          "image_url": "https://cdn.pandascore.co/images/lol/champion/image/95cd950f-61c7-430f-b731-4cc14ae5ad46.png",
                          "name": "Ryze",
                          "slug": "Ryze"
                        },
                        "creep_score": 315,
                        "cs_at_14": 153,
                        "cs_diff_at_14": 39,
                        "deaths": 2,
                        "flags": {
                          "first_blood_assist": false,
                          "first_blood_kill": false,
                          "first_inhibitor_assist": false,
                          "first_inhibitor_kill": true,
                          "first_tower_assist": true,
                          "first_tower_kill": false
                        },
                        "game_id": 270073,
                        "gold_earned": 15631,
                        "gold_percentage": 22.38,
                        "gold_spent": 14875,
                        "items": [
                          {
                            "id": 2678,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                            "is_trinket": true,
                            "name": "Farsight Alteration"
                          },
                          {
                            "id": 3933,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/0e746b55-4251-4a8f-a358-f1a83285d465.png",
                            "is_trinket": false,
                            "name": "Seeker's Armguard"
                          },
                          {
                            "id": 3948,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/43be86c8-4a8a-4d54-9cbc-d06045cf8f7a.png",
                            "is_trinket": false,
                            "name": "Seraph's Embrace"
                          },
                          {
                            "id": 4007,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/5104bf1a-4489-482b-81dc-d5106d64abf6.png",
                            "is_trinket": false,
                            "name": "Cosmic Drive"
                          },
                          {
                            "id": 4379,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/d8ec2fd4-b5d8-4611-a9df-81d2b2602922.png",
                            "is_trinket": false,
                            "name": "Chainlaced Crushers"
                          },
                          {
                            "id": 4619,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/ac14a5f7-88e7-4947-92bf-19eaac83ff3f.png",
                            "is_trinket": false,
                            "name": "Rod of Ages"
                          }
                        ],
                        "kills": 6,
                        "kills_counters": {
                          "inhibitors": 1,
                          "neutral_minions": 35,
                          "neutral_minions_enemy_jungle": 8,
                          "neutral_minions_team_jungle": 8,
                          "players": 6,
                          "turrets": 1,
                          "wards": 6
                        },
                        "kills_series": {
                          "double_kills": 0,
                          "penta_kills": 0,
                          "quadra_kills": 0,
                          "triple_kills": 0
                        },
                        "largest_critical_strike": 0,
                        "largest_killing_spree": 5,
                        "largest_multi_kill": 1,
                        "level": 18,
                        "magic_damage": {
                          "dealt": 261262,
                          "dealt_percentage": 76.69,
                          "dealt_to_champions": 29828,
                          "dealt_to_champions_percentage": 66.96,
                          "taken": 8213
                        },
                        "masteries": [],
                        "minions_killed": 315,
                        "opponent": {
                          "acronym": "TL",
                          "dark_mode_image_url": "https://cdn.pandascore.co/dark_images/team/dark_image/390/463px_team_liquid_2024_full_darkmode.png",
                          "id": 390,
                          "image_url": "https://cdn.pandascore.co/images/team/image/390/463px_team_liquid_2024_full_lightmode.png",
                          "location": "NL",
                          "modified_at": "2025-09-24T14:31:31Z",
                          "name": "Team Liquid",
                          "slug": "liquid"
                        },
                        "physical_damage": {
                          "dealt": 16026,
                          "dealt_percentage": 2.91,
                          "dealt_to_champions": 1486,
                          "dealt_to_champions_percentage": 2.86,
                          "taken": 13269
                        },
                        "player": {
                          "active": true,
                          "age": 21,
                          "birthday": "2004-04-27",
                          "first_name": "Lim",
                          "id": 38348,
                          "image_url": "https://cdn.pandascore.co/images/player/image/38348/100_t_quid_2025_split_3.png",
                          "last_name": "Hyeon-seung",
                          "modified_at": "2025-09-24T08:57:45Z",
                          "name": "Quid",
                          "nationality": "KR",
                          "role": "mid",
                          "slug": "quid"
                        },
                        "player_id": 38348,
                        "role": "mid",
                        "runes": [],
                        "runes_reforged": {
                          "primary_path": {
                            "id": 5,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/fedb6f0ca24988f397ad65670e1f9f76.png",
                            "keystone": {
                              "id": 54,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/4ee4739ae4a9cbf7be59650f92009edc.png",
                              "name": "Phase Rush",
                              "type": "keystone"
                            },
                            "lesser_runes": [
                              {
                                "id": 56,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/ce8144471d3d5b3ab7b13ceede28480f.png",
                                "name": "Manaflow Band",
                                "type": "slot1"
                              },
                              {
                                "id": 59,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/732d4e2a7fdf6ecc3ec8e42504a111b9.png",
                                "name": "Celerity",
                                "type": "slot2"
                              },
                              {
                                "id": 61,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/c34c227ecf5a2cb963ecde2005474d29.png",
                                "name": "Scorch",
                                "type": "slot3"
                              }
                            ],
                            "name": "Sorcery",
                            "type": "path"
                          },
                          "secondary_path": {
                            "id": 3,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                            "lesser_runes": [
                              {
                                "id": 79,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/1aee7893-608a-4293-b086-51b9fe3d0073.png",
                                "name": "Legend: Haste",
                                "type": "slot2"
                              },
                              {
                                "id": 38,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/08f4edce2a6f85edbfea701c04314cb9.png",
                                "name": "Cut Down",
                                "type": "slot3"
                              }
                            ],
                            "name": "Precision",
                            "type": "path"
                          },
                          "shards": {
                            "defense": {
                              "id": 72,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/82ecde52-ce41-4d3f-9e2c-f8fa940376a5.png",
                              "name": "Health",
                              "type": "shard"
                            },
                            "flex": {
                              "id": 73,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/18f82b15-e05c-4c85-a0ea-9c8e6812b5de.png",
                              "name": "Move Speed",
                              "type": "shard"
                            },
                            "offense": {
                              "id": 69,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                              "name": "Attack Speed",
                              "type": "shard"
                            }
                          }
                        },
                        "spells": [
                          {
                            "id": 134,
                            "image_url": "https://cdn.pandascore.co/images/lol/spell/image/7daefb32-5286-4b7a-83d5-b1ced1000769.png",
                            "name": "Flash"
                          },
                          {
                            "id": 139,
                            "image_url": "https://cdn.pandascore.co/images/lol/spell/image/8a267861-63a9-4867-bfc2-3f2e06c11445.png",
                            "name": "Teleport"
                          }
                        ],
                        "team": {
                          "acronym": "100",
                          "dark_mode_image_url": "https://cdn.pandascore.co/dark_images/team/dark_image/1537/190px_100_thieves_darkmode.png",
                          "id": 1537,
                          "image_url": "https://cdn.pandascore.co/images/team/image/1537/100_thieves_alternatelogo_square.png",
                          "location": "US",
                          "modified_at": "2025-09-24T08:57:45Z",
                          "name": "100 Thieves",
                          "slug": "100-thieves"
                        },
                        "total_damage": {
                          "dealt": 280761,
                          "dealt_percentage": 27.82,
                          "dealt_to_champions": 33334,
                          "dealt_to_champions_percentage": 31.58,
                          "taken": 23067
                        },
                        "total_heal": 5463,
                        "total_time_crowd_control_dealt": 121,
                        "total_units_healed": 1,
                        "true_damage": {
                          "dealt": 3472,
                          "dealt_percentage": 2.93,
                          "dealt_to_champions": 2019,
                          "dealt_to_champions_percentage": 22.2,
                          "taken": 1584
                        },
                        "wards": {
                          "placed": 20,
                          "sight_wards_bought_in_game": 0,
                          "vision_wards_bought_in_game": 9
                        },
                        "wards_placed": 20
                      },
                      {
                        "assists": 4,
                        "champion": {
                          "id": 3743,
                          "image_url": "https://cdn.pandascore.co/images/lol/champion/image/e1604511-218e-4a8d-add8-2fd62f2c148b.png",
                          "name": "Poppy",
                          "slug": "Poppy"
                        },
                        "creep_score": 188,
                        "cs_at_14": 95,
                        "cs_diff_at_14": -5,
                        "deaths": 4,
                        "flags": {
                          "first_blood_assist": false,
                          "first_blood_kill": false,
                          "first_inhibitor_assist": false,
                          "first_inhibitor_kill": false,
                          "first_tower_assist": false,
                          "first_tower_kill": false
                        },
                        "game_id": 270073,
                        "gold_earned": 9952,
                        "gold_percentage": 17.61,
                        "gold_spent": 9800,
                        "items": [
                          {
                            "id": 2474,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                            "is_trinket": false,
                            "name": "Control Ward"
                          },
                          {
                            "id": 2679,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                            "is_trinket": true,
                            "name": "Oracle Lens"
                          },
                          {
                            "id": 3661,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/26d4c0a4-10da-412c-b8cd-41a457ad63b3.png",
                            "is_trinket": false,
                            "name": "Randuin's Omen"
                          },
                          {
                            "id": 3927,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/fb0c2aeb-55bc-4f67-93cb-71741d18e396.png",
                            "is_trinket": false,
                            "name": "Negatron Cloak"
                          },
                          {
                            "id": 3952,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/96efc69d-8c31-4db1-ae6f-b9ac66d9fb37.png",
                            "is_trinket": false,
                            "name": "Winged Moonplate"
                          },
                          {
                            "id": 4017,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/ff83fe5c-e751-4245-ba85-648a0b2f4fcf.png",
                            "is_trinket": false,
                            "name": "Sundered Sky"
                          },
                          {
                            "id": 4206,
                            "image_url": "https://cdn.pandascore.co/images/lol/item/image/d7bc469a-df47-420a-9c9e-f41a1cabf40b.png",
                            "is_trinket": false,
                            "name": "Mercury's Treads"
                          }
                        ],
                        "kills": 1,
                        "kills_counters": {
                          "inhibitors": 0,
                          "neutral_minions": 162,
                          "neutral_minions_enemy_jungle": 0,
                          "neutral_minions_team_jungle": 106,
                          "players": 1,
                          "turrets": 0,
                          "wards": 5
                        },
                        "kills_series": {
                          "double_kills": 0,
                          "penta_kills": 0,
                          "quadra_kills": 0,
                          "triple_kills": 0
                        },
                        "largest_critical_strike": 157,
                        "largest_killing_spree": 0,
                        "largest_multi_kill": 1,
                        "level": 14,
                        "magic_damage": {
                          "dealt": 4333,
                          "dealt_percentage": 1.92,
                          "dealt_to_champions": 631,
                          "dealt_to_champions_percentage": 1.47,
                          "taken": 16731
                        },
                        "masteries": [],
                        "minions_killed": 188,
                        "opponent": {
                          "acronym": "100",
                          "dark_mode_image_url": "https://cdn.pandascore.co/dark_images/team/dark_image/1537/190px_100_thieves_darkmode.png",
                          "id": 1537,
                          "image_url": "https://cdn.pandascore.co/images/team/image/1537/100_thieves_alternatelogo_square.png",
                          "location": "US",
                          "modified_at": "2025-09-24T08:57:45Z",
                          "name": "100 Thieves",
                          "slug": "100-thieves"
                        },
                        "physical_damage": {
                          "dealt": 158209,
                          "dealt_percentage": 32.01,
                          "dealt_to_champions": 8499,
                          "dealt_to_champions_percentage": 21.65,
                          "taken": 19057
                        },
                        "player": {
                          "active": true,
                          "age": 22,
                          "birthday": "2002-11-13",
                          "first_name": "Ganbat",
                          "id": 39425,
                          "image_url": "https://cdn.pandascore.co/images/player/image/39425/tl_yuuji_2025_split_3.png",
                          "last_name": "Ulziidelger",
                          "modified_at": "2025-08-30T19:14:19Z",
                          "name": "Yuuji",
                          "nationality": "MN",
                          "role": "jun",
                          "slug": "yuuji"
                        },
                        "player_id": 39425,
                        "role": "jun",
                        "runes": [],
                        "runes_reforged": {
                          "primary_path": {
                            "id": 5,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/fedb6f0ca24988f397ad65670e1f9f76.png",
                            "keystone": {
                              "id": 54,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/4ee4739ae4a9cbf7be59650f92009edc.png",
                              "name": "Phase Rush",
                              "type": "keystone"
                            },
                            "lesser_runes": [
                              {
                                "id": 57,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/59ba46a95f8b51739d4eb2179654cf7e.png",
                                "name": "Nimbus Cloak",
                                "type": "slot1"
                              },
                              {
                                "id": 58,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/632a47c2a88802029838e383a866feb1.png",
                                "name": "Transcendence",
                                "type": "slot2"
                              },
                              {
                                "id": 62,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/abb0332095ac959dacaa1ed0ad4ad5e2.png",
                                "name": "Waterwalking",
                                "type": "slot3"
                              }
                            ],
                            "name": "Sorcery",
                            "type": "path"
                          },
                          "secondary_path": {
                            "id": 2,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                            "lesser_runes": [
                              {
                                "id": 19,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/44b7c635b7abab80f429fc8d8bbf8718.png",
                                "name": "Magical Footwear",
                                "type": "slot1"
                              },
                              {
                                "id": 24,
                                "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                                "name": "Cosmic Insight",
                                "type": "slot3"
                              }
                            ],
                            "name": "Inspiration",
                            "type": "path"
                          },
                          "shards": {
                            "defense": {
                              "id": 72,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/82ecde52-ce41-4d3f-9e2c-f8fa940376a5.png",
                              "name": "Health",
                              "type": "shard"
                            },
                            "flex": {
                              "id": 71,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                              "name": "Adaptative Force",
                              "type": "shard"
                            },
                            "offense": {
                              "id": 71,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                              "name": "Adaptative Force",
                              "type": "shard"
                            }
                          }
                        },
                        "spells": [
                          {
                            "id": 134,
                            "image_url": "https://cdn.pandascore.co/images/lol/spell/image/7daefb32-5286-4b7a-83d5-b1ced1000769.png",
                            "name": "Flash"
                          },
                          {
                            "id": 138,
                            "image_url": "https://cdn.pandascore.co/images/lol/spell/image/ad094a10-953f-438b-a330-06978486c9bb.png",
                            "name": "Smite"
                          }
                        ],
                        "team": {
                          "acronym": "TL",
                          "dark_mode_image_url": "https://cdn.pandascore.co/dark_images/team/dark_image/390/463px_team_liquid_2024_full_darkmode.png",
                          "id": 390,
                          "image_url": "https://cdn.pandascore.co/images/team/image/390/463px_team_liquid_2024_full_lightmode.png",
                          "location": "NL",
                          "modified_at": "2025-09-24T14:31:31Z",
                          "name": "Team Liquid",
                          "slug": "liquid"
                        },
                        "total_damage": {
                          "dealt": 244223,
                          "dealt_percentage": 29.64,
                          "dealt_to_champions": 9752,
                          "dealt_to_champions_percentage": 10.92,
                          "taken": 37311
                        },
                        "total_heal": 15913,
                        "total_time_crowd_control_dealt": 846,
                        "total_units_healed": 1,
                        "true_damage": {
                          "dealt": 81679,
                          "dealt_percentage": 78.53,
                          "dealt_to_champions": 620,
                          "dealt_to_champions_percentage": 8.61,
                          "taken": 1522
                        },
                        "wards": {
                          "placed": 13,
                          "sight_wards_bought_in_game": 0,
                          "vision_wards_bought_in_game": 12
                        },
                        "wards_placed": 13
                      }
                    ],
                    "position": 3,
                    "status": "finished",
                    "teams": [
                      {
                        "atakhan_kills": 0,
                        "bans": [
                          3672,
                          3798,
                          3772,
                          3787,
                          3729
                        ],
                        "baron_kills": 0,
                        "chemtech_drake_kills": 0,
                        "cloud_drake_kills": 0,
                        "color": "blue",
                        "dragon_kills": 0,
                        "elder_drake_kills": 0,
                        "first_atakhan": false,
                        "first_baron": false,
                        "first_blood": true,
                        "first_dragon": false,
                        "first_herald": true,
                        "first_inhibitor": false,
                        "first_tower": false,
                        "first_voidgrub": true,
                        "gold_earned": 56501,
                        "herald_kills": 1,
                        "hextech_drake_kills": 0,
                        "infernal_drake_kills": 0,
                        "inhibitor_kills": 0,
                        "kills": 12,
                        "mountain_drake_kills": 0,
                        "ocean_drake_kills": 0,
                        "player_ids": [
                          32,
                          47,
                          32065,
                          33658,
                          39425
                        ],
                        "team": {
                          "acronym": "TL",
                          "dark_mode_image_url": "https://cdn.pandascore.co/dark_images/team/dark_image/390/463px_team_liquid_2024_full_darkmode.png",
                          "id": 390,
                          "image_url": "https://cdn.pandascore.co/images/team/image/390/463px_team_liquid_2024_full_lightmode.png",
                          "location": "NL",
                          "modified_at": "2025-09-24T14:31:31Z",
                          "name": "Team Liquid",
                          "slug": "liquid"
                        },
                        "tower_kills": 2,
                        "voidgrub_kills": 2
                      },
                      {
                        "atakhan_kills": 1,
                        "bans": [
                          3780,
                          3611,
                          3662,
                          3610,
                          3736
                        ],
                        "baron_kills": 1,
                        "chemtech_drake_kills": 1,
                        "cloud_drake_kills": 0,
                        "color": "red",
                        "dragon_kills": 4,
                        "elder_drake_kills": 0,
                        "first_atakhan": true,
                        "first_baron": true,
                        "first_blood": false,
                        "first_dragon": true,
                        "first_herald": false,
                        "first_inhibitor": true,
                        "first_tower": true,
                        "first_voidgrub": false,
                        "gold_earned": 69852,
                        "herald_kills": 0,
                        "hextech_drake_kills": 0,
                        "infernal_drake_kills": 1,
                        "inhibitor_kills": 1,
                        "kills": 25,
                        "mountain_drake_kills": 2,
                        "ocean_drake_kills": 0,
                        "player_ids": [
                          1612,
                          3468,
                          18026,
                          18099,
                          38348
                        ],
                        "team": {
                          "acronym": "100",
                          "dark_mode_image_url": "https://cdn.pandascore.co/dark_images/team/dark_image/1537/190px_100_thieves_darkmode.png",
                          "id": 1537,
                          "image_url": "https://cdn.pandascore.co/images/team/image/1537/100_thieves_alternatelogo_square.png",
                          "location": "US",
                          "modified_at": "2025-09-24T08:57:45Z",
                          "name": "100 Thieves",
                          "slug": "100-thieves"
                        },
                        "tower_kills": 9,
                        "voidgrub_kills": 0
                      }
                    ],
                    "winner": {
                      "id": 1537,
                      "type": "Team"
                    },
                    "winner_type": "Team"
                  }
                ]
              }
            },
            "schema": {
              "$ref": "#/components/schemas/LoLTeamLastGames"
            }
          }
        },
        "description": "A list of League-of-Legends games\n\nDeprecated fields:\n- players[].minions_killed\n"
      }
    },
    "schemas": {
      "LoLTeamLastGames": {
        "items": {
          "additionalProperties": false,
          "deprecated": false,
          "description": "A team's last game",
          "properties": {
            "begin_at": {
              "deprecated": false,
              "description": "The game begin time, UTC.\n`null` when the game status is `not_started`",
              "format": "date-time",
              "minLength": 1,
              "nullable": true,
              "title": "GameBeginAt",
              "type": "string"
            },
            "complete": {
              "description": "Whether When `true`, the game statistics are complete and will not be updated again",
              "title": "GameComplete",
              "type": "boolean"
            },
            "detailed_stats": {
              "description": "Whether historical data is available for the game",
              "title": "GameDetailedStats",
              "type": "boolean"
            },
            "end_at": {
              "deprecated": false,
              "description": "The game end time, UTC.\n`null` when the game status is not `finished`",
              "format": "date-time",
              "minLength": 1,
              "nullable": true,
              "title": "GameEndAt",
              "type": "string"
            },
            "finished": {
              "description": "Whether the game is finished",
              "title": "GameIsFinished",
              "type": "boolean"
            },
            "forfeit": {
              "description": "Whether the game has been forfeited",
              "title": "GameIsForfeit",
              "type": "boolean"
            },
            "id": {
              "description": "LoL game ID",
              "minimum": 1,
              "title": "LoLGameID",
              "type": "integer"
            },
            "length": {
              "deprecated": false,
              "description": "Duration of the game in seconds.\n`null` when the game status is not `finished`",
              "minimum": 0,
              "nullable": true,
              "title": "GameLength",
              "type": "integer"
            },
            "match_id": {
              "minimum": 1,
              "title": "MatchID",
              "type": "integer"
            },
            "players": {
              "deprecated": false,
              "items": {
                "additionalProperties": false,
                "deprecated": false,
                "description": "Player's data for a Game",
                "properties": {
                  "assists": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLAssistCount",
                    "type": "integer"
                  },
                  "champion": {
                    "additionalProperties": false,
                    "deprecated": false,
                    "nullable": true,
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
                  "creep_score": {
                    "deprecated": false,
                    "description": "The player's Creep Score (CS.)\n\nNB: Creep Score can be different that the number of minions killed because neutral monsters can give more score.",
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLCreepScore",
                    "type": "integer"
                  },
                  "cs_at_14": {
                    "deprecated": false,
                    "description": "The player's Creep Score (CS.) at 14minutes",
                    "minimum": 0,
                    "nullable": true,
                    "title": "LolCreepScoreAt14",
                    "type": "integer"
                  },
                  "cs_diff_at_14": {
                    "deprecated": false,
                    "description": "Player CS difference compared to their lane opponent at the 14th minute in-game",
                    "nullable": true,
                    "title": "LolCreepScoreDifferenceAt14",
                    "type": "number"
                  },
                  "deaths": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLDeathCount",
                    "type": "integer"
                  },
                  "flags": {
                    "additionalProperties": false,
                    "deprecated": false,
                    "properties": {
                      "first_blood_assist": {
                        "deprecated": false,
                        "description": "Whether player got first blood assist",
                        "nullable": true,
                        "title": "LoLGotFirstBloodAssist",
                        "type": "boolean"
                      },
                      "first_blood_kill": {
                        "deprecated": false,
                        "description": "Whether player got first blood kill",
                        "nullable": true,
                        "title": "LoLGotFirstBloodKill",
                        "type": "boolean"
                      },
                      "first_inhibitor_assist": {
                        "deprecated": false,
                        "description": "Whether player got first inhibitor assist",
                        "nullable": true,
                        "title": "LoLGotFirstInhibitorAssist",
                        "type": "boolean"
                      },
                      "first_inhibitor_kill": {
                        "deprecated": false,
                        "description": "Whether player got first inhibitor kill",
                        "nullable": true,
                        "title": "LoLGotFirstInhibitorKill",
                        "type": "boolean"
                      },
                      "first_tower_assist": {
                        "deprecated": false,
                        "description": "Whether player got first tower assist",
                        "nullable": true,
                        "title": "LoLGotGirstTowerAssist",
                        "type": "boolean"
                      },
                      "first_tower_kill": {
                        "deprecated": false,
                        "description": "Whether player got first tower kill",
                        "nullable": true,
                        "title": "LoLGotFirstTowerKill",
                        "type": "boolean"
                      }
                    },
                    "required": [
                      "first_blood_assist",
                      "first_blood_kill",
                      "first_inhibitor_assist",
                      "first_inhibitor_kill",
                      "first_tower_assist",
                      "first_tower_kill"
                    ],
                    "title": "LoLFlags",
                    "type": "object"
                  },
                  "game_id": {
                    "description": "LoL game ID",
                    "minimum": 1,
                    "title": "LoLGameID",
                    "type": "integer"
                  },
                  "gold_earned": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLGold",
                    "type": "integer"
                  },
                  "gold_percentage": {
                    "deprecated": false,
                    "description": "Percentage of gold the player had compared to the total gold of the team",
                    "maximum": 100,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLPlayerGoldErnedPercentage",
                    "type": "number"
                  },
                  "gold_spent": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLGold",
                    "type": "integer"
                  },
                  "items": {
                    "items": {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "id": {
                          "minimum": 1,
                          "title": "LoLItemID",
                          "type": "integer"
                        },
                        "image_url": {
                          "deprecated": false,
                          "format": "uri",
                          "nullable": true,
                          "title": "LoLItemImageURL",
                          "type": "string"
                        },
                        "is_trinket": {
                          "deprecated": false,
                          "description": "Whether item is a trinket",
                          "nullable": true,
                          "title": "LoLItemIsTrinket",
                          "type": "boolean"
                        },
                        "name": {
                          "title": "LoLItemName",
                          "type": "string"
                        }
                      },
                      "required": [
                        "id",
                        "image_url",
                        "is_trinket",
                        "name"
                      ],
                      "title": "BaseLoLItem",
                      "type": "object"
                    },
                    "title": "BaseLoLItems",
                    "type": "array"
                  },
                  "kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLKillCount",
                    "type": "integer"
                  },
                  "kills_counters": {
                    "additionalProperties": false,
                    "deprecated": false,
                    "properties": {
                      "inhibitors": {
                        "deprecated": false,
                        "description": "Number of inhibitors killed by the player",
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLInhibitorCount",
                        "type": "integer"
                      },
                      "neutral_minions": {
                        "deprecated": false,
                        "description": "Creep Score awarded for killing neutral minions.\n\nNB: This can be different than the actual number of neutral minions killed.",
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLNeutralMinionCount",
                        "type": "integer"
                      },
                      "neutral_minions_enemy_jungle": {
                        "deprecated": false,
                        "description": "Creep Score awarded for killing neutral minions in the player's enemy jungle.\n\nNB: This can be different than the actual number of neutral minions killed.",
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLNeutralMinionsEnemyJungleCount",
                        "type": "integer"
                      },
                      "neutral_minions_team_jungle": {
                        "deprecated": false,
                        "description": "Creep Score awarded for killing neutral minions in the player's team jungle.\n\nNB: This can be different than the actual number of neutral minions killed.",
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLNeutralMinionsTeamJungleCount",
                        "type": "integer"
                      },
                      "players": {
                        "deprecated": false,
                        "description": "Number of players killed",
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLPlayerCount",
                        "type": "integer"
                      },
                      "turrets": {
                        "deprecated": false,
                        "description": "Number of turrets killed",
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLTurretCount",
                        "type": "integer"
                      },
                      "wards": {
                        "deprecated": false,
                        "description": "Number of wards killed by the player",
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLWardCount",
                        "type": "integer"
                      }
                    },
                    "required": [
                      "inhibitors",
                      "neutral_minions",
                      "neutral_minions_enemy_jungle",
                      "neutral_minions_team_jungle",
                      "players",
                      "turrets",
                      "wards"
                    ],
                    "title": "LoLKillCounters",
                    "type": "object"
                  },
                  "kills_series": {
                    "additionalProperties": false,
                    "deprecated": false,
                    "properties": {
                      "double_kills": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLKillsSerieDouble",
                        "type": "integer"
                      },
                      "penta_kills": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLKillsSeriePenta",
                        "type": "integer"
                      },
                      "quadra_kills": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLKillsSerieQuadra",
                        "type": "integer"
                      },
                      "triple_kills": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLKillsSerieTriple",
                        "type": "integer"
                      }
                    },
                    "required": [
                      "double_kills",
                      "penta_kills",
                      "quadra_kills",
                      "triple_kills"
                    ],
                    "title": "LoLKillsSeries",
                    "type": "object"
                  },
                  "largest_critical_strike": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLLargestCriticalStrike",
                    "type": "integer"
                  },
                  "largest_killing_spree": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLLargestKillingSpree",
                    "type": "integer"
                  },
                  "largest_multi_kill": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLLargestMultiKill",
                    "type": "integer"
                  },
                  "level": {
                    "deprecated": false,
                    "minimum": 1,
                    "nullable": true,
                    "title": "LoLChampionLevel",
                    "type": "integer"
                  },
                  "magic_damage": {
                    "additionalProperties": false,
                    "deprecated": false,
                    "properties": {
                      "dealt": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLDamage",
                        "type": "integer"
                      },
                      "dealt_percentage": {
                        "deprecated": false,
                        "description": "Percentage of damage dealt the player had compared to the total damage of the team",
                        "maximum": 100,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLPlayerDamageDealtPercentage",
                        "type": "number"
                      },
                      "dealt_to_champions": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLDamage",
                        "type": "integer"
                      },
                      "dealt_to_champions_percentage": {
                        "deprecated": false,
                        "description": "Percentage of damage dealt to champions the player had compared to the total damage of the team",
                        "maximum": 100,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAverageDamageDealtToChampionsPercentage",
                        "type": "number"
                      },
                      "taken": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLDamage",
                        "type": "integer"
                      }
                    },
                    "required": [
                      "dealt",
                      "dealt_percentage",
                      "dealt_to_champions",
                      "dealt_to_champions_percentage",
                      "taken"
                    ],
                    "title": "LoLMagicDamage",
                    "type": "object"
                  },
                  "masteries": {
                    "items": {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "id": {
                          "minimum": 1,
                          "title": "LoLMasteryID",
                          "type": "integer"
                        },
                        "name": {
                          "title": "LoLMasteryName",
                          "type": "string"
                        }
                      },
                      "required": [
                        "id",
                        "name"
                      ],
                      "title": "LoLMastery",
                      "type": "object"
                    },
                    "title": "LoLMasteries",
                    "type": "array"
                  },
                  "minions_killed": {
                    "deprecated": true,
                    "description": "The player's Creep Score (CS.)",
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLMinionsKilled",
                    "type": "integer"
                  },
                  "opponent": {
                    "deprecated": false,
                    "nullable": true,
                    "oneOf": [
                      {
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
                      {
                        "additionalProperties": false,
                        "deprecated": false,
                        "properties": {
                          "acronym": {
                            "deprecated": false,
                            "nullable": true,
                            "title": "TeamAcronym",
                            "type": "string"
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
                          "dark_mode_image_url",
                          "id",
                          "image_url",
                          "location",
                          "modified_at",
                          "name",
                          "slug"
                        ],
                        "title": "BaseTeam",
                        "type": "object"
                      }
                    ],
                    "title": "BaseOpponent"
                  },
                  "physical_damage": {
                    "additionalProperties": false,
                    "deprecated": false,
                    "properties": {
                      "dealt": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLDamage",
                        "type": "integer"
                      },
                      "dealt_percentage": {
                        "deprecated": false,
                        "description": "Percentage of damage dealt the player had compared to the total damage of the team",
                        "maximum": 100,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLPlayerDamageDealtPercentage",
                        "type": "number"
                      },
                      "dealt_to_champions": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLDamage",
                        "type": "integer"
                      },
                      "dealt_to_champions_percentage": {
                        "deprecated": false,
                        "description": "Percentage of damage dealt to champions the player had compared to the total damage of the team",
                        "maximum": 100,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAverageDamageDealtToChampionsPercentage",
                        "type": "number"
                      },
                      "taken": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLDamage",
                        "type": "integer"
                      }
                    },
                    "required": [
                      "dealt",
                      "dealt_percentage",
                      "dealt_to_champions",
                      "dealt_to_champions_percentage",
                      "taken"
                    ],
                    "title": "LoLPhysicalDamage",
                    "type": "object"
                  },
                  "player": {
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
                  "player_id": {
                    "description": "ID of the player",
                    "minimum": 1,
                    "title": "PlayerID",
                    "type": "integer"
                  },
                  "role": {
                    "deprecated": false,
                    "enum": [
                      "adc",
                      "jun",
                      "mid",
                      "sup",
                      "top"
                    ],
                    "nullable": true,
                    "title": "LoLPlayerRole",
                    "type": "string"
                  },
                  "runes": {
                    "items": {
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
                    "title": "LoLRunes",
                    "type": "array"
                  },
                  "runes_reforged": {
                    "additionalProperties": false,
                    "deprecated": false,
                    "properties": {
                      "primary_path": {
                        "additionalProperties": false,
                        "deprecated": false,
                        "nullable": true,
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
                          "keystone": {
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
                          "lesser_runes": {
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
                          "keystone",
                          "lesser_runes",
                          "name",
                          "type"
                        ],
                        "title": "LoLPlayerPrimaryRunePath",
                        "type": "object"
                      },
                      "secondary_path": {
                        "additionalProperties": false,
                        "deprecated": false,
                        "nullable": true,
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
                          "lesser_runes": {
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
                          "lesser_runes",
                          "name",
                          "type"
                        ],
                        "title": "LoLPlayerSecondaryRunePath",
                        "type": "object"
                      },
                      "shards": {
                        "additionalProperties": false,
                        "deprecated": false,
                        "properties": {
                          "defense": {
                            "additionalProperties": false,
                            "deprecated": false,
                            "nullable": true,
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
                          "flex": {
                            "additionalProperties": false,
                            "deprecated": false,
                            "nullable": true,
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
                          "offense": {
                            "additionalProperties": false,
                            "deprecated": false,
                            "nullable": true,
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
                          }
                        },
                        "required": [
                          "defense",
                          "flex",
                          "offense"
                        ],
                        "title": "LoLPlayerRuneShards",
                        "type": "object"
                      }
                    },
                    "required": [
                      "primary_path",
                      "secondary_path",
                      "shards"
                    ],
                    "title": "LoLPlayerRunesReforged",
                    "type": "object"
                  },
                  "spells": {
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
                  "team": {
                    "additionalProperties": false,
                    "deprecated": false,
                    "properties": {
                      "acronym": {
                        "deprecated": false,
                        "nullable": true,
                        "title": "TeamAcronym",
                        "type": "string"
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
                      "dark_mode_image_url",
                      "id",
                      "image_url",
                      "location",
                      "modified_at",
                      "name",
                      "slug"
                    ],
                    "title": "BaseTeam",
                    "type": "object"
                  },
                  "total_damage": {
                    "additionalProperties": false,
                    "deprecated": false,
                    "properties": {
                      "dealt": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLDamage",
                        "type": "integer"
                      },
                      "dealt_percentage": {
                        "deprecated": false,
                        "description": "Percentage of damage dealt the player had compared to the total damage of the team",
                        "maximum": 100,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLPlayerDamageDealtPercentage",
                        "type": "number"
                      },
                      "dealt_to_champions": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLDamage",
                        "type": "integer"
                      },
                      "dealt_to_champions_percentage": {
                        "deprecated": false,
                        "description": "Percentage of damage dealt to champions the player had compared to the total damage of the team",
                        "maximum": 100,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAverageDamageDealtToChampionsPercentage",
                        "type": "number"
                      },
                      "taken": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLDamage",
                        "type": "integer"
                      }
                    },
                    "required": [
                      "dealt",
                      "dealt_percentage",
                      "dealt_to_champions",
                      "dealt_to_champions_percentage",
                      "taken"
                    ],
                    "title": "LoLTotalDamage",
                    "type": "object"
                  },
                  "total_heal": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLTotalHeal",
                    "type": "integer"
                  },
                  "total_time_crowd_control_dealt": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLTotalTimeCrowdControlDealt",
                    "type": "integer"
                  },
                  "total_units_healed": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLTotalUnitsHealed",
                    "type": "integer"
                  },
                  "true_damage": {
                    "additionalProperties": false,
                    "deprecated": false,
                    "properties": {
                      "dealt": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLDamage",
                        "type": "integer"
                      },
                      "dealt_percentage": {
                        "deprecated": false,
                        "description": "Percentage of damage dealt the player had compared to the total damage of the team",
                        "maximum": 100,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLPlayerDamageDealtPercentage",
                        "type": "number"
                      },
                      "dealt_to_champions": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLDamage",
                        "type": "integer"
                      },
                      "dealt_to_champions_percentage": {
                        "deprecated": false,
                        "description": "Percentage of damage dealt to champions the player had compared to the total damage of the team",
                        "maximum": 100,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAverageDamageDealtToChampionsPercentage",
                        "type": "number"
                      },
                      "taken": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLDamage",
                        "type": "integer"
                      }
                    },
                    "required": [
                      "dealt",
                      "dealt_percentage",
                      "dealt_to_champions",
                      "dealt_to_champions_percentage",
                      "taken"
                    ],
                    "title": "LoLTrueDamage",
                    "type": "object"
                  },
                  "wards": {
                    "additionalProperties": false,
                    "deprecated": false,
                    "properties": {
                      "placed": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLWardsPlaced",
                        "type": "integer"
                      },
                      "sight_wards_bought_in_game": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLSightWards",
                        "type": "integer"
                      },
                      "vision_wards_bought_in_game": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLVisionWards",
                        "type": "integer"
                      }
                    },
                    "required": [
                      "placed",
                      "sight_wards_bought_in_game",
                      "vision_wards_bought_in_game"
                    ],
                    "title": "LoLWards",
                    "type": "object"
                  },
                  "wards_placed": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLWardsPlaced",
                    "type": "integer"
                  }
                },
                "required": [
                  "assists",
                  "champion",
                  "creep_score",
                  "cs_at_14",
                  "cs_diff_at_14",
                  "deaths",
                  "flags",
                  "game_id",
                  "gold_earned",
                  "gold_percentage",
                  "gold_spent",
                  "items",
                  "kills",
                  "kills_counters",
                  "kills_series",
                  "largest_critical_strike",
                  "largest_killing_spree",
                  "largest_multi_kill",
                  "level",
                  "magic_damage",
                  "masteries",
                  "minions_killed",
                  "opponent",
                  "physical_damage",
                  "player",
                  "player_id",
                  "role",
                  "runes",
                  "runes_reforged",
                  "spells",
                  "team",
                  "total_damage",
                  "total_heal",
                  "total_time_crowd_control_dealt",
                  "total_units_healed",
                  "true_damage",
                  "wards",
                  "wards_placed"
                ],
                "title": "LoLGamePlayer",
                "type": "object"
              },
              "nullable": true,
              "title": "LoLGamePlayers",
              "type": "array"
            },
            "position": {
              "description": "Game position in the match. Starts at 1",
              "minimum": 1,
              "title": "GamePosition",
              "type": "integer"
            },
            "status": {
              "description": "The game status",
              "enum": [
                "finished",
                "not_played",
                "not_started",
                "running"
              ],
              "title": "GameStatus",
              "type": "string"
            },
            "teams": {
              "deprecated": false,
              "items": {
                "additionalProperties": false,
                "deprecated": false,
                "description": "Team's data for a Game",
                "properties": {
                  "atakhan_kills": {
                    "deprecated": false,
                    "description": "The number of Atakhan killed by a team.",
                    "maximum": 1,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLAtakhanKills",
                    "type": "integer"
                  },
                  "bans": {
                    "items": {
                      "minimum": 1,
                      "title": "LoLChampionID",
                      "type": "integer"
                    },
                    "title": "LoLChampionIDs",
                    "type": "array"
                  },
                  "baron_kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLBaronKills",
                    "type": "integer"
                  },
                  "chemtech_drake_kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLChemtechDrakeKills",
                    "type": "integer"
                  },
                  "cloud_drake_kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLCloudDrakeKills",
                    "type": "integer"
                  },
                  "color": {
                    "enum": [
                      "blue",
                      "red"
                    ],
                    "title": "LoLTeamColor",
                    "type": "string"
                  },
                  "dragon_kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLDragonKills",
                    "type": "integer"
                  },
                  "elder_drake_kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLElderDrakeKills",
                    "type": "integer"
                  },
                  "first_atakhan": {
                    "deprecated": false,
                    "description": "Whether team killed the first Atakhan",
                    "nullable": true,
                    "title": "LoLTeamGotFirstAtakhan",
                    "type": "boolean"
                  },
                  "first_baron": {
                    "deprecated": false,
                    "description": "Whether team got first baron Nashor",
                    "nullable": true,
                    "title": "LoLTeamGotFirstBaron",
                    "type": "boolean"
                  },
                  "first_blood": {
                    "deprecated": false,
                    "description": "Whether team got first blood",
                    "nullable": true,
                    "title": "LoLTeamGotFirstBlood",
                    "type": "boolean"
                  },
                  "first_dragon": {
                    "deprecated": false,
                    "description": "Whether team got first dragon",
                    "nullable": true,
                    "title": "LoLTeamGotFirstDragon",
                    "type": "boolean"
                  },
                  "first_herald": {
                    "deprecated": false,
                    "description": "Whether team got first herald",
                    "nullable": true,
                    "title": "LoLTeamGotFirstHerald",
                    "type": "boolean"
                  },
                  "first_inhibitor": {
                    "deprecated": false,
                    "description": "Whether team got first inhibitor",
                    "nullable": true,
                    "title": "LoLTeamGotFirstInhibitor",
                    "type": "boolean"
                  },
                  "first_tower": {
                    "deprecated": false,
                    "description": "Whether team got first tower",
                    "nullable": true,
                    "title": "LoLTeamGotFirstTower",
                    "type": "boolean"
                  },
                  "first_voidgrub": {
                    "deprecated": false,
                    "description": "Whether team killed the first voidgrub",
                    "nullable": true,
                    "title": "LoLTeamGotFirstVoidgrub",
                    "type": "boolean"
                  },
                  "gold_earned": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLGold",
                    "type": "integer"
                  },
                  "herald_kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLHeraldKills",
                    "type": "integer"
                  },
                  "hextech_drake_kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLHextechDrakeKills",
                    "type": "integer"
                  },
                  "infernal_drake_kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLInfernalDrakeKills",
                    "type": "integer"
                  },
                  "inhibitor_kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLInhibitorKills",
                    "type": "integer"
                  },
                  "kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLKillCount",
                    "type": "integer"
                  },
                  "mountain_drake_kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLMountainDrakeKills",
                    "type": "integer"
                  },
                  "ocean_drake_kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLOceanDrakeKills",
                    "type": "integer"
                  },
                  "player_ids": {
                    "items": {
                      "description": "ID of the player",
                      "minimum": 1,
                      "title": "PlayerID",
                      "type": "integer"
                    },
                    "title": "PlayerIDs",
                    "type": "array"
                  },
                  "team": {
                    "additionalProperties": false,
                    "deprecated": false,
                    "properties": {
                      "acronym": {
                        "deprecated": false,
                        "nullable": true,
                        "title": "TeamAcronym",
                        "type": "string"
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
                      "dark_mode_image_url",
                      "id",
                      "image_url",
                      "location",
                      "modified_at",
                      "name",
                      "slug"
                    ],
                    "title": "BaseTeam",
                    "type": "object"
                  },
                  "tower_kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLTowerKills",
                    "type": "integer"
                  },
                  "voidgrub_kills": {
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
                  "atakhan_kills",
                  "bans",
                  "baron_kills",
                  "chemtech_drake_kills",
                  "cloud_drake_kills",
                  "color",
                  "dragon_kills",
                  "elder_drake_kills",
                  "first_atakhan",
                  "first_baron",
                  "first_blood",
                  "first_dragon",
                  "first_herald",
                  "first_inhibitor",
                  "first_tower",
                  "first_voidgrub",
                  "gold_earned",
                  "herald_kills",
                  "hextech_drake_kills",
                  "infernal_drake_kills",
                  "inhibitor_kills",
                  "kills",
                  "mountain_drake_kills",
                  "ocean_drake_kills",
                  "player_ids",
                  "team",
                  "tower_kills",
                  "voidgrub_kills"
                ],
                "title": "LoLGameTeam",
                "type": "object"
              },
              "nullable": true,
              "title": "LoLGameTeams",
              "type": "array"
            },
            "winner": {
              "additionalProperties": false,
              "deprecated": false,
              "properties": {
                "id": {
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
                "type": {
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
                "id",
                "type"
              ],
              "title": "GameWinner",
              "type": "object"
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
            "complete",
            "detailed_stats",
            "end_at",
            "finished",
            "forfeit",
            "id",
            "length",
            "match_id",
            "players",
            "position",
            "status",
            "teams",
            "winner",
            "winner_type"
          ],
          "title": "LoLTeamLastGame",
          "type": "object"
        },
        "title": "LoLTeamLastGames",
        "type": "array"
      },
      "TeamIDOrSlug": {
        "description": "A team ID or slug",
        "oneOf": [
          {
            "description": "The ID of the team.",
            "minimum": 1,
            "title": "TeamID",
            "type": "integer"
          },
          {
            "minLength": 1,
            "pattern": "^[a-z0-9_-]+$",
            "title": "TeamSlug",
            "type": "string"
          }
        ],
        "title": "TeamIDOrSlug"
      },
      "filter_over_LoLTeamLastGames": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "begin_at": {
            "items": {
              "description": "The game begin time, UTC.\n`null` when the game status is `not_started`",
              "format": "date-time",
              "minLength": 1,
              "title": "GameBeginAt",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "complete": {
            "description": "Whether When `true`, the game statistics are complete and will not be updated again",
            "title": "GameComplete",
            "type": "boolean"
          },
          "detailed_stats": {
            "description": "Whether historical data is available for the game",
            "title": "GameDetailedStats",
            "type": "boolean"
          },
          "end_at": {
            "items": {
              "description": "The game end time, UTC.\n`null` when the game status is not `finished`",
              "format": "date-time",
              "minLength": 1,
              "title": "GameEndAt",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "finished": {
            "description": "Whether the game is finished",
            "title": "GameIsFinished",
            "type": "boolean"
          },
          "forfeit": {
            "description": "Whether the game has been forfeited",
            "title": "GameIsForfeit",
            "type": "boolean"
          },
          "id": {
            "items": {
              "description": "LoL game ID",
              "minimum": 1,
              "title": "LoLGameID",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "length": {
            "items": {
              "description": "Duration of the game in seconds.\n`null` when the game status is not `finished`",
              "minimum": 0,
              "title": "GameLength",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "match_id": {
            "items": {
              "minimum": 1,
              "title": "MatchID",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "position": {
            "items": {
              "description": "Game position in the match. Starts at 1",
              "minimum": 1,
              "title": "GamePosition",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "status": {
            "items": {
              "description": "The game status",
              "enum": [
                "finished",
                "not_played",
                "not_started",
                "running"
              ],
              "title": "GameStatus",
              "type": "string"
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
          }
        },
        "type": "object"
      },
      "range_over_LoLTeamLastGames": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "begin_at": {
            "items": {
              "description": "The game begin time, UTC.\n`null` when the game status is `not_started`",
              "format": "date-time",
              "minLength": 1,
              "title": "GameBeginAt",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "complete": {
            "items": {
              "description": "Whether When `true`, the game statistics are complete and will not be updated again",
              "title": "GameComplete",
              "type": "boolean"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "detailed_stats": {
            "items": {
              "description": "Whether historical data is available for the game",
              "title": "GameDetailedStats",
              "type": "boolean"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "end_at": {
            "items": {
              "description": "The game end time, UTC.\n`null` when the game status is not `finished`",
              "format": "date-time",
              "minLength": 1,
              "title": "GameEndAt",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "finished": {
            "items": {
              "description": "Whether the game is finished",
              "title": "GameIsFinished",
              "type": "boolean"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "forfeit": {
            "items": {
              "description": "Whether the game has been forfeited",
              "title": "GameIsForfeit",
              "type": "boolean"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "id": {
            "items": {
              "description": "LoL game ID",
              "minimum": 1,
              "title": "LoLGameID",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "length": {
            "items": {
              "description": "Duration of the game in seconds.\n`null` when the game status is not `finished`",
              "minimum": 0,
              "title": "GameLength",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "match_id": {
            "items": {
              "minimum": 1,
              "title": "MatchID",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "position": {
            "items": {
              "description": "Game position in the match. Starts at 1",
              "minimum": 1,
              "title": "GamePosition",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "status": {
            "items": {
              "description": "The game status",
              "enum": [
                "finished",
                "not_played",
                "not_started",
                "running"
              ],
              "title": "GameStatus",
              "type": "string"
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
          }
        },
        "type": "object"
      },
      "search_over_LoLTeamLastGames": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "status": {
            "description": "The game status",
            "enum": [
              "finished",
              "not_played",
              "not_started",
              "running"
            ],
            "title": "GameStatus",
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
      "sort_over_LoLTeamLastGames": {
        "items": {
          "enum": [
            "begin_at",
            "-begin_at",
            "complete",
            "-complete",
            "detailed_stats",
            "-detailed_stats",
            "end_at",
            "-end_at",
            "finished",
            "-finished",
            "forfeit",
            "-forfeit",
            "id",
            "-id",
            "length",
            "-length",
            "match_id",
            "-match_id",
            "position",
            "-position",
            "status",
            "-status",
            "winner_type",
            "-winner_type"
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
    "/lol/teams/{team_id_or_slug}/games": {
      "get": {
        "description": "List finished games for a given League of Legends team\n> ℹ️  \n> \n> This endpoint is only available to customers with a historical or real-time data plan",
        "operationId": "get_lol_teams_teamIdOrSlug_games",
        "parameters": [
          {
            "description": "A team ID or slug",
            "in": "path",
            "name": "team_id_or_slug",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/TeamIDOrSlug"
            }
          },
          {
            "description": "Options to filter results. String fields are case sensitive\nFor more information on filtering, see [docs](/docs/filtering-and-sorting#filter).",
            "explode": true,
            "in": "query",
            "name": "filter",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/filter_over_LoLTeamLastGames"
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
              "$ref": "#/components/schemas/range_over_LoLTeamLastGames"
            },
            "style": "deepObject"
          },
          {
            "description": "Options to sort results\nFor more information on sorting, see [docs](/docs/filtering-and-sorting#sort).",
            "in": "query",
            "name": "sort",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/sort_over_LoLTeamLastGames"
            }
          },
          {
            "description": "Options to search results\nFor more information on searching, see [docs](/docs/filtering-and-sorting#search).",
            "explode": true,
            "in": "query",
            "name": "search",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/search_over_LoLTeamLastGames"
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
            "$ref": "#/components/responses/LoLTeamLastGames"
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
        "summary": "List finished games for a given team",
        "tags": [
          "LoL games"
        ],
        "x-pandascore-plan": "Historical plan",
        "x-readme": {
          "code-samples": [
            {
              "code": "curl --request GET \\\n     --url 'https://api.pandascore.co/lol/teams/{team_id_or_slug}/games' \\\n     --header 'accept: application/json'\n",
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