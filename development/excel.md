# Excel

## Core Functions  

- `SUMIF(range, criteria, [sum_range])`  
- `COUNTIF(range, criteria)`  
- `VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])`  
- `COUNT()` (counts numbers)  
- `COUNTA()` (counts non-empty cells)  
- `SEQUENCE(rows, [columns], start, step)` *(dynamic array)*  

## lookup/match  

- `MATCH(lookup_value, lookup_array, [match_type])`  
- `INDEX(array, row_num, [column_num])`  

---

## Data Validation (Dropdown)  

1. Select cell(s)  
2. **Data > Data Validation**  
3. Set:  
   - Allow: *List*  
   - Source: comma-separated values or cell range  

---

## Shortcut

### Delete Blank Rows  

1. `Ctrl + G` > **Go To Special** > *Blanks*  
2. `Ctrl + -` (minus) > Delete **entire row**  

### Convert to Table  

- `Ctrl + T` (create structured table)  

---

## Formatting Tips  

- **Column/Row Size**: Right-click > *Row Height/Column Width* (use multiples of 5)  
- **Borders**: Home > *Border Buttons* or remove via *Clear Borders*  
- **Sheet Tab Color**: Right-click sheet tab > *Tab Color*  
- **Freeze Header**: Click row 2 > **View > Freeze Panes**  
- **Zebra Striping**:  
  `Conditional Formatting` > *New Rule* >  
  Formula: `=MOD(ROW(),2)`  
