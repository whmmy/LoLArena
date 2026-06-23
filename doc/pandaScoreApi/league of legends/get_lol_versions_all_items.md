> ## Documentation Index
> Fetch the complete documentation index at: https://developers.pandascore.co/llms.txt
> Use this file to discover all available pages before exploring further.

# List items for all version

Deprecated. Equivalent route: [/lol/items?filter[videogame_version]=all](/reference/get_lol_items)
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
      "LoLItems": {
        "content": {
          "application/json": {
            "examples": {
              "/lol/items?page[size]=1": {
                "description": "/lol/items?page[size]=1",
                "value": [
                  {
                    "flat_armor_mod": 0,
                    "flat_crit_chance_mod": 0,
                    "flat_hp_pool_mod": 300,
                    "flat_hp_regen_mod": 0,
                    "flat_magic_damage_mod": 90,
                    "flat_movement_speed_mod": 0,
                    "flat_mp_pool_mod": 0,
                    "flat_mp_regen_mod": 0,
                    "flat_physical_damage_mod": 0,
                    "flat_spell_block_mod": null,
                    "gold_base": 815,
                    "gold_purchasable": true,
                    "gold_sell": 2240,
                    "gold_total": 3200,
                    "id": 3029,
                    "image_url": "https://cdn.pandascore.co/images/lol/item/image/d8bc76803ce35849f47bda2b7310e555.png",
                    "is_trinket": false,
                    "name": "Night Harvester",
                    "percent_attack_speed_mod": 0,
                    "percent_life_steal_mod": 0,
                    "percent_movement_speed_mod": 0,
                    "videogame_versions": [
                      "12.12.1"
                    ]
                  }
                ]
              }
            },
            "schema": {
              "$ref": "#/components/schemas/LoLItems"
            }
          }
        },
        "description": "A list of League-of-Legends items"
      }
    },
    "schemas": {
      "LoLItems": {
        "items": {
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
        "title": "LoLItems",
        "type": "array"
      },
      "filter_over_LoLItems": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "flat_armor_mod": {
            "items": {
              "minimum": 0,
              "title": "LoLFlatArmorMod",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "flat_crit_chance_mod": {
            "items": {
              "minimum": 0,
              "title": "LoLFlatCritChanceMod",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "flat_hp_pool_mod": {
            "items": {
              "minimum": 0,
              "title": "LoLFlatHPPoolMod",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "flat_hp_regen_mod": {
            "items": {
              "minimum": 0,
              "title": "LoLFlatHPRegenMod",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "flat_magic_damage_mod": {
            "items": {
              "minimum": 0,
              "title": "LoLFlatMagicDamageMod",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "flat_movement_speed_mod": {
            "items": {
              "minimum": 0,
              "title": "LoLFlatMovementSpeedMod",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "flat_mp_pool_mod": {
            "items": {
              "minimum": 0,
              "title": "LoLFlatMPPoolMod",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "flat_mp_regen_mod": {
            "items": {
              "minimum": 0,
              "title": "LoLFlatMPRegenMod",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "flat_physical_damage_mod": {
            "items": {
              "minimum": 0,
              "title": "LoLFlatPhysicalDamageMod",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "flat_spell_block_mod": {
            "items": {
              "minimum": 0,
              "title": "LoLFlatSpellBlockMod",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "gold_base": {
            "items": {
              "minimum": 0,
              "title": "LoLGold",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "gold_purchasable": {
            "description": "Whether gold can be bought",
            "title": "LoLGoldPurchasable",
            "type": "boolean"
          },
          "gold_sell": {
            "items": {
              "minimum": 0,
              "title": "LoLGold",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "gold_total": {
            "items": {
              "minimum": 0,
              "title": "LoLGold",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "id": {
            "items": {
              "minimum": 1,
              "title": "LoLItemID",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "name": {
            "items": {
              "title": "LoLItemName",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "percent_attack_speed_mod": {
            "items": {
              "minimum": 0,
              "title": "LoLPercentAttackSpeedMod",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "percent_life_steal_mod": {
            "items": {
              "minimum": 0,
              "title": "LoLPercentLifeStealMod",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "percent_movement_speed_mod": {
            "items": {
              "minimum": 0,
              "title": "LoLPercentMovementSpeedMod",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "trinket": {
            "description": "Whether item is a trinket",
            "title": "LoLItemIsTrinket",
            "type": "boolean"
          },
          "videogame_version": {
            "description": "Filter by the names of videogame versions, all versions using `filter[videogame_version]=all`, or by the latest version using `filter[videogame_version]=latest`"
          }
        },
        "type": "object"
      },
      "range_over_LoLItems": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "flat_armor_mod": {
            "items": {
              "minimum": 0,
              "title": "LoLFlatArmorMod",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "flat_crit_chance_mod": {
            "items": {
              "minimum": 0,
              "title": "LoLFlatCritChanceMod",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "flat_hp_pool_mod": {
            "items": {
              "minimum": 0,
              "title": "LoLFlatHPPoolMod",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "flat_hp_regen_mod": {
            "items": {
              "minimum": 0,
              "title": "LoLFlatHPRegenMod",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "flat_magic_damage_mod": {
            "items": {
              "minimum": 0,
              "title": "LoLFlatMagicDamageMod",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "flat_movement_speed_mod": {
            "items": {
              "minimum": 0,
              "title": "LoLFlatMovementSpeedMod",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "flat_mp_pool_mod": {
            "items": {
              "minimum": 0,
              "title": "LoLFlatMPPoolMod",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "flat_mp_regen_mod": {
            "items": {
              "minimum": 0,
              "title": "LoLFlatMPRegenMod",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "flat_physical_damage_mod": {
            "items": {
              "minimum": 0,
              "title": "LoLFlatPhysicalDamageMod",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "flat_spell_block_mod": {
            "items": {
              "minimum": 0,
              "title": "LoLFlatSpellBlockMod",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "gold_base": {
            "items": {
              "minimum": 0,
              "title": "LoLGold",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "gold_purchasable": {
            "items": {
              "description": "Whether gold can be bought",
              "title": "LoLGoldPurchasable",
              "type": "boolean"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "gold_sell": {
            "items": {
              "minimum": 0,
              "title": "LoLGold",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "gold_total": {
            "items": {
              "minimum": 0,
              "title": "LoLGold",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "id": {
            "items": {
              "minimum": 1,
              "title": "LoLItemID",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "name": {
            "items": {
              "title": "LoLItemName",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "percent_attack_speed_mod": {
            "items": {
              "minimum": 0,
              "title": "LoLPercentAttackSpeedMod",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "percent_life_steal_mod": {
            "items": {
              "minimum": 0,
              "title": "LoLPercentLifeStealMod",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "percent_movement_speed_mod": {
            "items": {
              "minimum": 0,
              "title": "LoLPercentMovementSpeedMod",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          }
        },
        "type": "object"
      },
      "search_over_LoLItems": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "name": {
            "title": "LoLItemName",
            "type": "string"
          }
        },
        "type": "object"
      },
      "sort_over_LoLItems": {
        "items": {
          "enum": [
            "flat_armor_mod",
            "-flat_armor_mod",
            "flat_crit_chance_mod",
            "-flat_crit_chance_mod",
            "flat_hp_pool_mod",
            "-flat_hp_pool_mod",
            "flat_hp_regen_mod",
            "-flat_hp_regen_mod",
            "flat_magic_damage_mod",
            "-flat_magic_damage_mod",
            "flat_movement_speed_mod",
            "-flat_movement_speed_mod",
            "flat_mp_pool_mod",
            "-flat_mp_pool_mod",
            "flat_mp_regen_mod",
            "-flat_mp_regen_mod",
            "flat_physical_damage_mod",
            "-flat_physical_damage_mod",
            "flat_spell_block_mod",
            "-flat_spell_block_mod",
            "gold_base",
            "-gold_base",
            "gold_purchasable",
            "-gold_purchasable",
            "gold_sell",
            "-gold_sell",
            "gold_total",
            "-gold_total",
            "id",
            "-id",
            "name",
            "-name",
            "percent_attack_speed_mod",
            "-percent_attack_speed_mod",
            "percent_life_steal_mod",
            "-percent_life_steal_mod",
            "percent_movement_speed_mod",
            "-percent_movement_speed_mod"
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
    "/lol/versions/all/items": {
      "get": {
        "deprecated": true,
        "description": "Deprecated. Equivalent route: [/lol/items?filter[videogame_version]=all](/reference/get_lol_items)\n> ℹ️  \n> \n> This endpoint is available to all customers",
        "operationId": "get_lol_versions_all_items",
        "parameters": [
          {
            "description": "Options to filter results. String fields are case sensitive\nFor more information on filtering, see [docs](/docs/filtering-and-sorting#filter).",
            "explode": true,
            "in": "query",
            "name": "filter",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/filter_over_LoLItems"
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
              "$ref": "#/components/schemas/range_over_LoLItems"
            },
            "style": "deepObject"
          },
          {
            "description": "Options to sort results\nFor more information on sorting, see [docs](/docs/filtering-and-sorting#sort).",
            "in": "query",
            "name": "sort",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/sort_over_LoLItems"
            }
          },
          {
            "description": "Options to search results\nFor more information on searching, see [docs](/docs/filtering-and-sorting#search).",
            "explode": true,
            "in": "query",
            "name": "search",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/search_over_LoLItems"
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
            "$ref": "#/components/responses/LoLItems"
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
        "summary": "List items for all version",
        "tags": [
          "LoL items"
        ],
        "x-readme": {
          "code-samples": [
            {
              "code": "curl --request GET \\\n     --url 'https://api.pandascore.co/lol/versions/all/items' \\\n     --header 'accept: application/json'\n",
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