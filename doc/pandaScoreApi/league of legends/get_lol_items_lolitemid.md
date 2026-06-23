> ## Documentation Index
> Fetch the complete documentation index at: https://developers.pandascore.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Get an item

Get a single item by ID or by slug
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
      "LoLItem": {
        "content": {
          "application/json": {
            "examples": {
              "/lol/items/2297": {
                "description": "/lol/items/2297",
                "value": {
                  "flat_armor_mod": 0,
                  "flat_crit_chance_mod": 0,
                  "flat_hp_pool_mod": 300,
                  "flat_hp_regen_mod": 0,
                  "flat_magic_damage_mod": 75,
                  "flat_movement_speed_mod": 0,
                  "flat_mp_pool_mod": 0,
                  "flat_mp_regen_mod": 0,
                  "flat_physical_damage_mod": 0,
                  "flat_spell_block_mod": null,
                  "gold_base": 750,
                  "gold_purchasable": true,
                  "gold_sell": 2170,
                  "gold_total": 3100,
                  "id": 2297,
                  "image_url": "https://cdn.pandascore.co/images/lol/item/image/994d1f8fe18f9c8699c6156eec280eca.png",
                  "is_trinket": false,
                  "name": "Liandry's Torment",
                  "percent_attack_speed_mod": 0,
                  "percent_life_steal_mod": 0,
                  "percent_movement_speed_mod": 0,
                  "videogame_versions": [
                    "10.22.1",
                    "10.21.1",
                    "10.20.1",
                    "10.19.1",
                    "10.18.1",
                    "10.16.1",
                    "10.15.1",
                    "10.14.1",
                    "10.13.1",
                    "10.12.1",
                    "10.11.1",
                    "10.10.3216176",
                    "10.10.3208608",
                    "10.9.1",
                    "10.8.1",
                    "10.7.1",
                    "10.6.1",
                    "10.5.1",
                    "10.4.1",
                    "10.3.1",
                    "10.2.1",
                    "10.1.1",
                    "9.24.2",
                    "9.24.1",
                    "9.23.1",
                    "9.22.1",
                    "9.21.1",
                    "9.20.1",
                    "9.19.1",
                    "9.18.1",
                    "9.17.1",
                    "9.16.1",
                    "9.15.1",
                    "9.14.1",
                    "9.13.1",
                    "9.12.1",
                    "9.11.1",
                    "9.10.1",
                    "9.9.1",
                    "9.8.1",
                    "9.7.2",
                    "9.7.1",
                    "9.6.1",
                    "9.5.1",
                    "9.4.1",
                    "9.3.1",
                    "9.2.1",
                    "9.1.1",
                    "8.24.1",
                    "8.23.1",
                    "8.22.1",
                    "8.20.1",
                    "8.19.1"
                  ]
                }
              }
            },
            "schema": {
              "$ref": "#/components/schemas/LoLItem"
            }
          }
        },
        "description": "A League-of-Legends item"
      }
    },
    "schemas": {
      "LoLItem": {
        "additionalProperties": false,
        "deprecated": false,
        "properties": {
          "flat_armor_mod": {
            "deprecated": false,
            "minimum": 0,
            "nullable": true,
            "title": "LoLFlatArmorMod",
            "type": "integer"
          },
          "flat_crit_chance_mod": {
            "deprecated": false,
            "minimum": 0,
            "nullable": true,
            "title": "LoLFlatCritChanceMod",
            "type": "integer"
          },
          "flat_hp_pool_mod": {
            "deprecated": false,
            "minimum": 0,
            "nullable": true,
            "title": "LoLFlatHPPoolMod",
            "type": "integer"
          },
          "flat_hp_regen_mod": {
            "deprecated": false,
            "minimum": 0,
            "nullable": true,
            "title": "LoLFlatHPRegenMod",
            "type": "integer"
          },
          "flat_magic_damage_mod": {
            "deprecated": false,
            "minimum": 0,
            "nullable": true,
            "title": "LoLFlatMagicDamageMod",
            "type": "integer"
          },
          "flat_movement_speed_mod": {
            "deprecated": false,
            "minimum": 0,
            "nullable": true,
            "title": "LoLFlatMovementSpeedMod",
            "type": "integer"
          },
          "flat_mp_pool_mod": {
            "deprecated": false,
            "minimum": 0,
            "nullable": true,
            "title": "LoLFlatMPPoolMod",
            "type": "integer"
          },
          "flat_mp_regen_mod": {
            "deprecated": false,
            "minimum": 0,
            "nullable": true,
            "title": "LoLFlatMPRegenMod",
            "type": "integer"
          },
          "flat_physical_damage_mod": {
            "deprecated": false,
            "minimum": 0,
            "nullable": true,
            "title": "LoLFlatPhysicalDamageMod",
            "type": "integer"
          },
          "flat_spell_block_mod": {
            "deprecated": false,
            "minimum": 0,
            "nullable": true,
            "title": "LoLFlatSpellBlockMod",
            "type": "integer"
          },
          "gold_base": {
            "deprecated": false,
            "minimum": 0,
            "nullable": true,
            "title": "LoLGold",
            "type": "integer"
          },
          "gold_purchasable": {
            "deprecated": false,
            "description": "Whether gold can be bought",
            "nullable": true,
            "title": "LoLGoldPurchasable",
            "type": "boolean"
          },
          "gold_sell": {
            "deprecated": false,
            "minimum": 0,
            "nullable": true,
            "title": "LoLGold",
            "type": "integer"
          },
          "gold_total": {
            "deprecated": false,
            "minimum": 0,
            "nullable": true,
            "title": "LoLGold",
            "type": "integer"
          },
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
          },
          "percent_attack_speed_mod": {
            "deprecated": false,
            "minimum": 0,
            "nullable": true,
            "title": "LoLPercentAttackSpeedMod",
            "type": "integer"
          },
          "percent_life_steal_mod": {
            "deprecated": false,
            "minimum": 0,
            "nullable": true,
            "title": "LoLPercentLifeStealMod",
            "type": "integer"
          },
          "percent_movement_speed_mod": {
            "deprecated": false,
            "minimum": 0,
            "nullable": true,
            "title": "LoLPercentMovementSpeedMod",
            "type": "integer"
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
          "flat_armor_mod",
          "flat_crit_chance_mod",
          "flat_hp_pool_mod",
          "flat_hp_regen_mod",
          "flat_magic_damage_mod",
          "flat_movement_speed_mod",
          "flat_mp_pool_mod",
          "flat_mp_regen_mod",
          "flat_physical_damage_mod",
          "flat_spell_block_mod",
          "gold_base",
          "gold_purchasable",
          "gold_sell",
          "gold_total",
          "id",
          "image_url",
          "is_trinket",
          "name",
          "percent_attack_speed_mod",
          "percent_life_steal_mod",
          "percent_movement_speed_mod",
          "videogame_versions"
        ],
        "title": "LoLItem",
        "type": "object"
      },
      "LoLItemID": {
        "minimum": 1,
        "title": "LoLItemID",
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
    "/lol/items/{lol_item_id}": {
      "get": {
        "description": "Get a single item by ID or by slug\n> ℹ️  \n> \n> This endpoint is available to all customers",
        "operationId": "get_lol_items_lolItemId",
        "parameters": [
          {
            "description": "An item ID",
            "in": "path",
            "name": "lol_item_id",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/LoLItemID"
            }
          }
        ],
        "responses": {
          "200": {
            "$ref": "#/components/responses/LoLItem"
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
        "summary": "Get an item",
        "tags": [
          "LoL items"
        ],
        "x-readme": {
          "code-samples": [
            {
              "code": "curl --request GET \\\n     --url 'https://api.pandascore.co/lol/items/{lol_item_id}' \\\n     --header 'accept: application/json'\n",
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