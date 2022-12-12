# read_SQL

## Overview

ModuleDescription

## Description

SQLite3からデータを取得するコンポーネント

### Input and Output



### Algorithm etc



### Basic Information

|  |  |
----|---- 
| Module Name | read_SQL |
| Description | ModuleDescription |
| Version | 1.2.0 |
| Vendor | Tsukasa Takahashi |
| Category | Category |
| Comp. Type | STATIC |
| Act. Type | PERIODIC |
| Kind | DataFlowComponent |
| MAX Inst. | 0 |

### Activity definition

<table>
  <tr>
    <td rowspan="4">on_initialize</td>
    <td colspan="2">implemented</td>
    <tr>
      <td>Description</td>
      <td></td>
    </tr>
    <tr>
      <td>PreCondition</td>
      <td></td>
    </tr>
    <tr>
      <td>PostCondition</td>
      <td></td>
    </tr>
  </tr>
  <tr>
    <td>on_finalize</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_startup</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_shutdown</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td rowspan="4">on_activated</td>
    <td colspan="2">implemented</td>
    <tr>
      <td>Description</td>
      <td></td>
    </tr>
    <tr>
      <td>PreCondition</td>
      <td></td>
    </tr>
    <tr>
      <td>PostCondition</td>
      <td></td>
    </tr>
  </tr>
  <tr>
    <td rowspan="4">on_deactivated</td>
    <td colspan="2">implemented</td>
    <tr>
      <td>Description</td>
      <td></td>
    </tr>
    <tr>
      <td>PreCondition</td>
      <td></td>
    </tr>
    <tr>
      <td>PostCondition</td>
      <td></td>
    </tr>
  </tr>
  <tr>
    <td rowspan="4">on_execute</td>
    <td colspan="2">implemented</td>
    <tr>
      <td>Description</td>
      <td></td>
    </tr>
    <tr>
      <td>PreCondition</td>
      <td></td>
    </tr>
    <tr>
      <td>PostCondition</td>
      <td></td>
    </tr>
  </tr>
  <tr>
    <td>on_aborting</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_error</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_reset</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_state_update</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_rate_changed</td>
    <td colspan="2"></td>
  </tr>
</table>

### InPorts definition


### OutPorts definition

#### db_out

SQLite3 Database<br/>SELECT * FROM {table_name}

<table>
  <tr>
    <td>DataType</td>
    <td>TaskListSeq</td>
    <td></td>
  </tr>
  <tr>
    <td>IDL file</td>
    <td colspan="2">TaskListSeq.idl</td>
  </tr>
  <tr>
    <td>Number of Data</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Semantics</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Unit</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Occirrence frecency Period</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Operational frecency Period</td>
    <td colspan="2"></td>
  </tr>
</table>


### Service Port definition


### Configuration definition

#### database_conf

データベースの相対パス, データベース内のテーブル名


<table>
  <tr>
    <td>DataType</td>
    <td colspan="2">string</td>
  </tr>
  <tr>
    <td>DefaultValue</td>
    <td>../tasklist.db', 'task</td>
    <td>../tasklist.db, task</td>
  </tr>
  <tr>
    <td>Unit</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Widget</td>
    <td colspan="2">text</td>
  </tr>
  <tr>
    <td>Step</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Constraint</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Range</td>
    <td colspan="2"></td>
  </tr>
</table>

#### sort

db_outの並べ替え


<table>
  <tr>
    <td>DataType</td>
    <td colspan="2">string</td>
  </tr>
  <tr>
    <td>DefaultValue</td>
    <td>start_time', 'ASC</td>
    <td>start_time', 'ASC</td>
  </tr>
  <tr>
    <td>Unit</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Widget</td>
    <td colspan="2">text</td>
  </tr>
  <tr>
    <td>Step</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Constraint</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Range</td>
    <td colspan="2">{coloum name}', '{ASC or DSC}</td>
  </tr>
</table>


## Demo

## Requirement

## Setup

### Windows

### Ubuntu

## Usage

## Running the tests

## LICENCE




## References




## Author


