# Industrial Management System (IMS) Software usage manual.
### Terms Acceptance (First Login Gate)

**What it Does:**  
Ensures users agree to legal terms before using the workspace.

**Navigation Path:**  
`Redirect Screen > Terms & Conditions Page > Accept`

**Visual Elements:**  
- Terms text panel  
- Consent checkbox/toggle  
- Confirmation button

**Step-by-Step Usage:**

1. Read the terms page shown after login.
2. Mark acceptance.
3. Submit to continue into the app.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** You must be signed in.
- **Automatic Effects:** Accepted status is saved to your profile.
- **Constraints:** You cannot access core pages until acceptance is complete.

**Data Recovery & Cleanup:**  
No recycle bin or restore flow applies.

**Troubleshooting (Common Blockers):**

- If you keep getting redirected here, acceptance was not saved. Re-submit and refresh.
- If the button does nothing, ensure the consent control is selected.

**Access Level:**  
Tenant users who are required to accept terms.

---

### Cash Account Setup (Required Before Regular Use)

**What it Does:**  
Creates the initial cash account so transactions and ledgers can work correctly.

**Navigation Path:**  
`Redirect Screen > Cash Account Setup > Save`

**Visual Elements:**  
- Opening balance input  
- Save/submit button  
- Success banner

**Step-by-Step Usage:**

1. Enter opening cash balance.
2. Submit the setup form.
3. Return to Dashboard.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Must be logged in and terms accepted.
- **Automatic Effects:** Enables normal access to transaction modules.
- **Constraints:** Opening balance cannot be negative.

**Data Recovery & Cleanup:**  
No trash/restore path shown for this setup flow.

**Troubleshooting (Common Blockers):**

- If redirected repeatedly, setup was not completed successfully.
- If save fails, check that balance is a valid non-negative number.

**Access Level:**  
Required for non-admin tenant users before normal module access.

---

### Dashboard Home

**What it Does:**  
Shows high-level business status and shortcuts to daily work.

**Navigation Path:**  
`Primary Sidebar > Dashboard`

**Visual Elements:**  
- Home icon in sidebar
- Top summary cards/charts (if enabled)
- Header page title

**Step-by-Step Usage:**

1. Click **Dashboard**.
2. Review key metrics and alerts.
3. Open detailed modules from sidebar as needed.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Account active, terms accepted, cash account ready (for applicable users).
- **Automatic Effects:** Loads role-based widgets and analytics where permitted.
- **Constraints:** Some analytics are hidden without analytics permission.

**Data Recovery & Cleanup:**  
Not applicable.

**Troubleshooting (Common Blockers):**

- If analytics panels are missing, your role likely lacks analytics access.
- If login loops, account may be inactive or blocked by prerequisites.

**Access Level:**  
Signed-in tenant users; advanced analytics visible only to permitted roles.

---

### Customer Management - Add Customer

**What it Does:**  
Creates customer profiles for sales, ledger tracking, and reporting.

**Navigation Path:**  
`Primary Sidebar > Customers > Add Customer`

**Visual Elements:**  
- Person icon next to Customers  
- Form fields (name, contact, opening balance, address)  
- Save/submit button

**Step-by-Step Usage:**

1. Open **Add Customer**.
2. Fill required and optional details.
3. Save to create the customer.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Customer permission required.
- **Automatic Effects:** New customer becomes selectable in sales and ledger screens.
- **Constraints:** Name length must be valid; opening balance cannot be negative; optional fields still have format/length limits.

**Data Recovery & Cleanup:**  
No user-facing trash/restore flow for customers.

**Troubleshooting (Common Blockers):**

- Save blocked if name is too short/long.
- Invalid phone/address formatting can trigger validation errors.

**Access Level:**  
Users with customer access permission.

---

### Customer Management - Customer List

**What it Does:**  
Displays all customers for review and further actions.

**Navigation Path:**  
`Primary Sidebar > Customers > Show All Customers`

**Visual Elements:**  
- Table/list view  
- Row-level action controls (view/edit where available)  
- Search/filter controls (if present in table UI)

**Step-by-Step Usage:**

1. Open **Show All Customers**.
2. Search or browse records.
3. Open a customer record for updates.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Customer permission required.
- **Automatic Effects:** List reflects tenant-specific records only.
- **Constraints:** Cross-tenant records are hidden/restricted.

**Data Recovery & Cleanup:**  
Deletion restore is not exposed in tenant UI.

**Troubleshooting (Common Blockers):**

- If records are missing, confirm you are in the correct tenant workspace.
- If actions are disabled, your role may not include edit privileges.

**Access Level:**  
Users with customer access permission.

---

### Customer Management - Edit Customer

**What it Does:**  
Updates customer details used across transactions and ledgers.

**Navigation Path:**  
`Primary Sidebar > Customers > Show All Customers > Edit (row action)`

**Visual Elements:**  
- Pre-filled form  
- Update/save button  
- Success or validation message area

**Step-by-Step Usage:**

1. Open the customer list.
2. Choose a customer and click edit.
3. Update fields and save.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Customer edit authorization.
- **Automatic Effects:** Updated details appear in future documents/references.
- **Constraints:** Same validation rules as creation apply.

**Data Recovery & Cleanup:**  
No separate version history/restore panel exposed.

**Troubleshooting (Common Blockers):**

- Edit denied when record is outside your allowed scope.
- Validation errors occur if updated values break field rules.

**Access Level:**  
Users with customer permission and edit rights.

---

### Customer Ledger

**What it Does:**  
Shows transaction history and balance movement per customer.

**Navigation Path:**  
`Primary Sidebar > Customers > Customer Ledger`

**Visual Elements:**  
- Ledger table  
- Date/filter inputs  
- Print option where available

**Step-by-Step Usage:**

1. Open **Customer Ledger**.
2. Select customer/date range.
3. Review entries or print report.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Customer permission.
- **Automatic Effects:** Pulls customer-linked financial entries.
- **Constraints:** Results depend on existing transaction history.

**Data Recovery & Cleanup:**  
Ledger is derived from transactions; restore is handled by source transaction policies, not ledger screen.

**Troubleshooting (Common Blockers):**

- Empty ledger often means no transactions in selected period.
- If print is blank, adjust filters and retry.

**Access Level:**  
Users with customer access permission.

---

### Supplier Management - Add Supplier

**What it Does:**  
Creates supplier records used in purchases and supplier payments.

**Navigation Path:**  
`Primary Sidebar > Supplier > Add Supplier`

**Visual Elements:**  
- Supplier form fields  
- Save button  
- Notification banner

**Step-by-Step Usage:**

1. Open **Add Supplier**.
2. Enter supplier details.
3. Save record.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Supplier permission.
- **Automatic Effects:** Supplier becomes available in purchase/payment modules.
- **Constraints:** Name and optional fields must pass length/format checks; opening value cannot be negative.

**Data Recovery & Cleanup:**  
No visible restore bin for suppliers.

**Troubleshooting (Common Blockers):**

- Save fails if required fields are incomplete.
- Invalid phone/address input can block submission.

**Access Level:**  
Users with supplier access permission.

---

### Supplier Management - Supplier List / Edit

**What it Does:**  
Lets users view and maintain supplier records.

**Navigation Path:**  
`Primary Sidebar > Supplier > Show All Suppliers > Edit (row action)`

**Visual Elements:**  
- Supplier table  
- Row action controls  
- Edit form with update button

**Step-by-Step Usage:**

1. Open supplier list.
2. Select supplier row action.
3. Update and save details.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Supplier access plus edit authorization.
- **Automatic Effects:** Updated supplier info flows to future purchasing/payment records.
- **Constraints:** Tenant scope and validation rules apply.

**Data Recovery & Cleanup:**  
No tenant-facing restore workflow found.

**Troubleshooting (Common Blockers):**

- Edit denied if record is outside your permitted scope.
- Validation errors mirror add-supplier rules.

**Access Level:**  
Users with supplier permission and edit rights.

---

### Supplier Ledger

**What it Does:**  
Provides supplier-side financial history and balances.

**Navigation Path:**  
`Primary Sidebar > Supplier > Supplier Ledger`

**Visual Elements:**  
- Ledger/report grid  
- Date/supplier filters  
- Print action

**Step-by-Step Usage:**

1. Open **Supplier Ledger**.
2. Select supplier and date range.
3. Review or print.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Supplier permission.
- **Automatic Effects:** Aggregates supplier-linked transactions.
- **Constraints:** Requires existing records to display meaningful output.

**Data Recovery & Cleanup:**  
No recycle bin at ledger level.

**Troubleshooting (Common Blockers):**

- No rows usually means no activity in selected range.
- Re-check filters before assuming data loss.

**Access Level:**  
Users with supplier access permission.

---

### Product Management - Add Product

**What it Does:**  
Adds saleable products to catalog and stock workflows.

**Navigation Path:**  
`Primary Sidebar > Product > Add Product`

**Visual Elements:**  
- Product form  
- Fields for name, price, quantity, description  
- Save button

**Step-by-Step Usage:**

1. Open **Add Product**.
2. Enter product details.
3. Save product.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Product permission.
- **Automatic Effects:** Product appears in sales and inventory-related selections.
- **Constraints:** Name required; numeric fields cannot be negative; description length limits apply.

**Data Recovery & Cleanup:**  
No exposed restore/trash path for deleted products.

**Troubleshooting (Common Blockers):**

- Submission fails for missing product name.
- Invalid numeric values (negative or non-numeric) block save.

**Access Level:**  
Users with product access permission.

---

### Product Management - Product List / Item Flow

**What it Does:**  
Shows products and movement history for stock tracking.

**Navigation Path:**  
- `Primary Sidebar > Product > Show All Products`  
- `Primary Sidebar > Product > Item Flow`

**Visual Elements:**  
- Product listing table  
- Flow/history table with filters  
- Row action controls

**Step-by-Step Usage:**

1. Open product list for catalog management.
2. Open **Item Flow** to trace movement history.
3. Filter and inspect records.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Product permission.
- **Automatic Effects:** Flow view reflects stock changes from multiple operational areas.
- **Constraints:** Data visibility remains tenant-scoped.

**Data Recovery & Cleanup:**  
No dedicated trash module surfaced for product records.

**Troubleshooting (Common Blockers):**

- Missing movement lines may be filter-related.
- If item flow is empty for new products, no transactions exist yet.

**Access Level:**  
Users with product access permission.

---

### Product Assembly - Create Assembly

**What it Does:**  
Combines components into assembled products for production workflows.

**Navigation Path:**  
`Primary Sidebar > Product > Assemble Product > Assemble Product`

**Visual Elements:**  
- Nested submenu under Product  
- Assembly form inputs  
- Save action

**Step-by-Step Usage:**

1. Expand **Product** then **Assemble Product**.
2. Open assembly create page.
3. Configure assembly and save.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Assembly permission in addition to base product access patterns.
- **Automatic Effects:** Assembly records influence product cost/history views.
- **Constraints:** Component relationships and quantities must be valid.

**Data Recovery & Cleanup:**  
No dedicated restore bin exposed in UI.

**Troubleshooting (Common Blockers):**

- Menu not visible if assembly permission is missing.
- Save errors usually indicate incomplete or inconsistent component setup.

**Access Level:**  
Users with product-assembly permission.

---

### Product Assembly - Price History

**What it Does:**  
Shows historical assembly pricing for audit and costing review.

**Navigation Path:**  
`Primary Sidebar > Product > Assemble Product > Product Price History`

**Visual Elements:**  
- History list/table  
- Filter controls  
- Detail links (if present)

**Step-by-Step Usage:**

1. Open **Product Price History**.
2. Filter by product/time.
3. Review trends and previous values.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Assembly permission.
- **Automatic Effects:** History is generated from assembly operations.
- **Constraints:** Only records with existing assembly history appear.

**Data Recovery & Cleanup:**  
Historical entries are read-focused; no restore action exposed.

**Troubleshooting (Common Blockers):**

- Empty list means no assembly history in selected criteria.

**Access Level:**  
Users with product-assembly permission.

---

### Raw Product Management - Add Raw Product

**What it Does:**  
Creates raw material records used in purchasing and assembly.

**Navigation Path:**  
`Primary Sidebar > Raw Product > Add Raw Product`

**Visual Elements:**  
- Raw product form  
- Save button  
- Confirmation message

**Step-by-Step Usage:**

1. Open **Add Raw Product**.
2. Enter details.
3. Save.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Raw-product permission.
- **Automatic Effects:** Raw item becomes selectable in purchase/assembly flows.
- **Constraints:** Standard field validation and tenant-scoping apply.

**Data Recovery & Cleanup:**  
No tenant trash/restore page surfaced.

**Troubleshooting (Common Blockers):**

- Save blocked by missing required fields or invalid formats.

**Access Level:**  
Users with raw-product access permission.

---

### Raw Product Management - Raw Product List

**What it Does:**  
Displays all raw material records for maintenance and lookup.

**Navigation Path:**  
`Primary Sidebar > Raw Product > Show All Raw Products`

**Visual Elements:**  
- List/table view  
- Row action controls  
- Search/filter tools

**Step-by-Step Usage:**

1. Open raw product list.
2. Search and review records.
3. Perform available row actions.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Raw-product permission.
- **Automatic Effects:** Tenant-specific records only.
- **Constraints:** Cross-tenant records are not accessible.

**Data Recovery & Cleanup:**  
No dedicated recovery/trash route exposed.

**Troubleshooting (Common Blockers):**

- If expected items are absent, verify workspace/tenant and filters.

**Access Level:**  
Users with raw-product access permission.

---

### Purchase Workflow - Create Purchase

**What it Does:**  
Records incoming stock from suppliers.

**Navigation Path:**  
- `Primary Sidebar > Purchases > Raw Product Purchase > Add Purchase`  
- `Primary Sidebar > Purchases > Sale Product Purchase > Add Purchase`

**Visual Elements:**  
- Multi-level purchase submenu  
- Purchase form with supplier/items/payment fields  
- Save button

**Step-by-Step Usage:**

1. Choose the correct purchase type branch.
2. Open **Add Purchase**.
3. Enter supplier and item details.
4. Save purchase.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Purchase permission.
- **Automatic Effects:** Updates stock and financial records connected to purchase workflows.
- **Constraints:** Required fields and valid numeric values are mandatory.

**Data Recovery & Cleanup:**  
No general restore bin for deleted purchases.

**Troubleshooting (Common Blockers):**

- Wrong branch selection (raw vs sale product purchase) causes mismatched item context.
- Save failures usually indicate missing supplier/items or invalid totals.

**Access Level:**  
Users with purchase access permission.

---

### Purchase Workflow - Purchase List

**What it Does:**  
Shows recorded purchases for review, print, and lifecycle actions.

**Navigation Path:**  
- `Primary Sidebar > Purchases > Raw Product Purchase > Purchase List`  
- `Primary Sidebar > Purchases > Sale Product Purchase > Purchase List`

**Visual Elements:**  
- Purchase table  
- Row action menu/buttons  
- Status and totals columns

**Step-by-Step Usage:**

1. Open **Purchase List** from the correct branch.
2. Find record using filters/search.
3. Open details or print as needed.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Purchase permission.
- **Automatic Effects:** List reflects tenant and purchase-type context.
- **Constraints:** Cross-tenant records are restricted.

**Data Recovery & Cleanup:**  
Deleted purchase records do not expose a standard restore menu.

**Troubleshooting (Common Blockers):**

- If expected purchase is missing, verify purchase-type branch and date filters.

**Access Level:**  
Users with purchase access permission.

---

### Purchase Workflow - Print Purchase Document

**What it Does:**  
Generates a print-friendly purchase document.

**Navigation Path:**  
`Primary Sidebar > Purchases > Purchase List > Print (row action)`

**Visual Elements:**  
- Print page layout  
- Browser print action  
- Header/footer invoice content

**Step-by-Step Usage:**

1. Open purchase list.
2. Select print for a purchase.
3. Print or export from browser.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Purchase record must exist and be accessible.
- **Automatic Effects:** No data changes; output only.
- **Constraints:** Inaccessible records cannot be printed.

**Data Recovery & Cleanup:**  
Not applicable.

**Troubleshooting (Common Blockers):**

- Print fails if record was deleted or outside your authorization scope.

**Access Level:**  
Users with purchase access permission.

---

### Purchase Return - Create Return

**What it Does:**  
Records items returned against prior purchases.

**Navigation Path:**  
- `Primary Sidebar > Purchases > Raw Product Purchase > Add Purchase Return`  
- `Primary Sidebar > Purchases > Sale Product Purchase > Add Purchase Return`

**Visual Elements:**  
- Return form  
- Source purchase selector  
- Item/quantity fields  
- Submit button

**Step-by-Step Usage:**

1. Open **Add Purchase Return** in the correct branch.
2. Select source purchase.
3. Enter returned items and quantities.
4. Save return.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Purchase permission and valid source purchase.
- **Automatic Effects:** Adjusts stock/financial impact per return workflow.
- **Constraints:** Returned items must match selected purchase context.

**Data Recovery & Cleanup:**  
No dedicated restore bin found for purchase returns.

**Troubleshooting (Common Blockers):**

- Return item list may stay empty if source purchase is not selected/valid.
- Submission errors often indicate invalid item mapping or quantities.

**Access Level:**  
Users with purchase access permission.

---

### Purchase Return - Return List

**What it Does:**  
Shows all purchase return entries for tracking and review.

**Navigation Path:**  
- `Primary Sidebar > Purchases > Raw Product Purchase > Purchase Return List`  
- `Primary Sidebar > Purchases > Sale Product Purchase > Purchase Return List`

**Visual Elements:**  
- Return table  
- Filter/search tools  
- Row action controls

**Step-by-Step Usage:**

1. Open return list in the appropriate branch.
2. Locate a return using filters.
3. Review details and available actions.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Purchase permission.
- **Automatic Effects:** Data remains branch-specific by purchase type.
- **Constraints:** Tenant-scope restrictions apply.

**Data Recovery & Cleanup:**  
No visible restore flow for return deletions.

**Troubleshooting (Common Blockers):**

- If data appears incomplete, verify branch, date, and supplier filters.

**Access Level:**  
Users with purchase access permission.

---

### Sales Workflow - Add Sale

**What it Does:**  
Creates sales transactions and invoice-ready customer billing records.

**Navigation Path:**  
`Primary Sidebar > Sales > Add Sale`

**Visual Elements:**  
- Sales form  
- Customer/product selectors  
- Totals panel  
- Save/submit button

**Step-by-Step Usage:**

1. Open **Add Sale**.
2. Select customer and products.
3. Confirm amounts/payment details.
4. Save sale.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Sales permission and valid products/customers.
- **Automatic Effects:** Updates stock and financial ledgers based on sale.
- **Constraints:** Invalid quantities or incomplete required fields block submission.

**Data Recovery & Cleanup:**  
No standard restore bin for deleted sales.

**Troubleshooting (Common Blockers):**

- Submission failures often come from incomplete item/payment details.
- If stock-linked errors appear, review quantities and item availability.

**Access Level:**  
Users with sales access permission.

---

### Sales Workflow - Sales List

**What it Does:**  
Displays all sales with access to review and further actions.

**Navigation Path:**  
`Primary Sidebar > Sales > Sales List`

**Visual Elements:**  
- Sales table  
- Action controls per row  
- Search/filter area

**Step-by-Step Usage:**

1. Open **Sales List**.
2. Filter/find transaction.
3. Open print/return/other available actions.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Sales permission.
- **Automatic Effects:** Shows tenant-scoped records only.
- **Constraints:** Hidden/blocked actions depend on permissions and record state.

**Data Recovery & Cleanup:**  
Deleted sales do not expose tenant restore screens.

**Troubleshooting (Common Blockers):**

- Missing rows are often due to filters or tenant context mismatch.

**Access Level:**  
Users with sales access permission.

---

### Sales Workflow - Print Sale Invoice

**What it Does:**  
Creates printable customer invoices using your selected invoice template style.

**Navigation Path:**  
`Primary Sidebar > Sales > Sales List > Print (row action)`

**Visual Elements:**  
- Print preview style (template-dependent)  
- Header/customer/items/totals layout  
- Browser print controls

**Step-by-Step Usage:**

1. Open sales list.
2. Click print on a sale.
3. Print or export from browser.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Sales record exists and is accessible.
- **Automatic Effects:** Uses your current invoice template preference for visual format.
- **Constraints:** If template setting is missing/invalid, output may fallback or fail visually.

**Data Recovery & Cleanup:**  
Not applicable.

**Troubleshooting (Common Blockers):**

- Unexpected invoice look: verify selected template under Settings > Invoice Templates.

**Access Level:**  
Users with sales access permission.

---

### Sales Return - Add Sale Return

**What it Does:**  
Processes customer returns against original sales.

**Navigation Path:**  
`Primary Sidebar > Sales > Add Sale Return`

**Visual Elements:**  
- Return form  
- Source sale selector  
- Item/quantity fields  
- Submit button

**Step-by-Step Usage:**

1. Open **Add Sale Return**.
2. Choose original sale.
3. Enter return quantities and notes.
4. Save return.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Sales permission and valid source sale.
- **Automatic Effects:** Adjusts stock and return-related financial impact.
- **Constraints:** Return items must map to source sale context.

**Data Recovery & Cleanup:**  
No dedicated restore bin surfaced for sale returns.

**Troubleshooting (Common Blockers):**

- Empty return items usually means source sale is not selected or not eligible.

**Access Level:**  
Users with sales access permission.

---

### Sales Return - Return List

**What it Does:**  
Shows all sales return transactions for tracking and audit.

**Navigation Path:**  
`Primary Sidebar > Sales > Sales Return List`

**Visual Elements:**  
- Return table  
- Search/filter controls  
- Row actions

**Step-by-Step Usage:**

1. Open **Sales Return List**.
2. Filter to required date/customer.
3. Review records and details.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Sales permission.
- **Automatic Effects:** Data is tenant-scoped.
- **Constraints:** Records outside your scope are hidden/blocked.

**Data Recovery & Cleanup:**  
No user-facing restore workflow found.

**Troubleshooting (Common Blockers):**

- Missing records are commonly filter-related.

**Access Level:**  
Users with sales access permission.

---

### Customer Recovery - Add Recovery Entry

**What it Does:**  
Records customer payment recovery activity (not a recycle bin function).

**Navigation Path:**  
`Primary Sidebar > Recovery > Add Recovery`

**Visual Elements:**  
- Recovery form  
- Customer selection  
- Amount/date inputs

**Step-by-Step Usage:**

1. Open **Add Recovery**.
2. Select customer and enter payment details.
3. Save recovery.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Recovery permission.
- **Automatic Effects:** Updates customer financial tracking.
- **Constraints:** Amount/date and linked data must be valid.

**Data Recovery & Cleanup:**  
This module is financial recovery; it is not a deleted-item restore area.

**Troubleshooting (Common Blockers):**

- If customer-specific history is missing, verify selected customer and prior transactions.

**Access Level:**  
Users with recovery access permission.

---

### Customer Recovery - Recovery List

**What it Does:**  
Lists all customer recovery entries for review.

**Navigation Path:**  
`Primary Sidebar > Recovery > Show All Recoveries`

**Visual Elements:**  
- Recovery table  
- Filters  
- Row actions

**Step-by-Step Usage:**

1. Open **Show All Recoveries**.
2. Use filters and inspect entries.
3. Open actions as needed.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Recovery permission.
- **Automatic Effects:** Reflects tenant-specific recovery records.
- **Constraints:** Scope and record-level permissions apply.

**Data Recovery & Cleanup:**  
No restore bin for deleted recovery records was surfaced.

**Troubleshooting (Common Blockers):**

- Empty results are typically date/filter selection issues.

**Access Level:**  
Users with recovery access permission.

---

### Expense Management - Add New Expense

**What it Does:**  
Captures business expenses with category/type tracking.

**Navigation Path:**  
`Primary Sidebar > Expense > Add New Expense`

**Visual Elements:**  
- Expense form  
- Type/name dropdowns  
- Amount/date fields  
- Submit button

**Step-by-Step Usage:**

1. Open **Add New Expense**.
2. Select expense type and matching expense name.
3. Enter amount/date and optional notes/bank.
4. Save entry.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Expense permission.
- **Automatic Effects:** Posts expense to financial records.
- **Constraints:** Amount must be non-negative; date format must be valid; selected expense name must belong to selected expense type; optional bank must belong to your tenant workspace; notes length has a limit.

**Data Recovery & Cleanup:**  
No user-facing restore bin for deleted expenses.

**Troubleshooting (Common Blockers):**

- Mismatch between expense type and expense name is a common error.
- Invalid date format blocks submission.

**Access Level:**  
Users with expense access permission.

---

### Expense Management - Expense List

**What it Does:**  
Displays historical expense records for auditing and updates.

**Navigation Path:**  
`Primary Sidebar > Expense > Expense List`

**Visual Elements:**  
- Expense table  
- Filter/search controls  
- Row actions

**Step-by-Step Usage:**

1. Open **Expense List**.
2. Filter records by date/category.
3. Review details and available actions.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Expense permission.
- **Automatic Effects:** Tenant-only records are shown.
- **Constraints:** Visibility follows role and tenant scope.

**Data Recovery & Cleanup:**  
No restore/trash page surfaced for expense records.

**Troubleshooting (Common Blockers):**

- If records appear missing, verify filters and date range.

**Access Level:**  
Users with expense access permission.

---

### Cash Operations - Cash Account Page

**What it Does:**  
Maintains ongoing cash account settings and opening/working balances.

**Navigation Path:**  
`Primary Sidebar > Cash > Cash Account`

**Visual Elements:**  
- Cash menu with dollar icon  
- Account form/details panel  
- Update button

**Step-by-Step Usage:**

1. Open **Cash Account**.
2. Review/update available fields.
3. Save changes.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Cash permission and existing cash account.
- **Automatic Effects:** Changes affect downstream cash-based reports/flows.
- **Constraints:** Numeric constraints apply to cash values.

**Data Recovery & Cleanup:**  
No dedicated restore history in UI.

**Troubleshooting (Common Blockers):**

- If inaccessible, ensure initial cash setup was completed and role includes cash access.

**Access Level:**  
Users with cash access permission.

---

### Cash Operations - Cash to Bank Transfer

**What it Does:**  
Moves funds from cash account into a selected bank account.

**Navigation Path:**  
`Primary Sidebar > Cash > Cash to Bank`

**Visual Elements:**  
- Transfer form  
- Source/destination fields  
- Amount input  
- Submit button

**Step-by-Step Usage:**

1. Open **Cash to Bank**.
2. Select destination bank and amount.
3. Submit transfer.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Cash permission; bank records available.
- **Automatic Effects:** Updates both cash and bank books.
- **Constraints:** Transfer amounts must be valid and non-negative.

**Data Recovery & Cleanup:**  
No end-user restore flow for transfer deletions.

**Troubleshooting (Common Blockers):**

- Transfer errors may occur if bank selection is invalid or amount is malformed.

**Access Level:**  
Users with cash access permission.

---

### Cash Operations - Cash Book

**What it Does:**  
Shows chronological cash movements for reconciliation.

**Navigation Path:**  
`Primary Sidebar > Cash > Cash Book`

**Visual Elements:**  
- Ledger-style table  
- Date filters  
- Totals summary area

**Step-by-Step Usage:**

1. Open **Cash Book**.
2. Select date range/filter.
3. Review entries and totals.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Cash permission.
- **Automatic Effects:** Pulls transaction-linked cash movements.
- **Constraints:** Output depends on existing transactions and selected range.

**Data Recovery & Cleanup:**  
Derived report; no separate restore flow.

**Troubleshooting (Common Blockers):**

- Empty report often means no transactions in selected period.

**Access Level:**  
Users with cash access permission.

---

### Bank Operations - Add New Bank

**What it Does:**  
Creates bank accounts for transfers and ledger tracking.

**Navigation Path:**  
`Primary Sidebar > Bank > Add New Bank`

**Visual Elements:**  
- Bank form  
- Account number field  
- Save button

**Step-by-Step Usage:**

1. Open **Add New Bank**.
2. Enter bank and account details.
3. Save account.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Bank permission.
- **Automatic Effects:** New bank becomes available in transfer and expense flows.
- **Constraints:** Account number must be unique; opening values cannot be negative.

**Data Recovery & Cleanup:**  
No visible restore/trash flow for bank accounts.

**Troubleshooting (Common Blockers):**

- Duplicate account number blocks submission.

**Access Level:**  
Users with bank access permission.

---

### Bank Operations - Show All Banks / Edit Bank

**What it Does:**  
Lists bank accounts and allows bank record updates.

**Navigation Path:**  
`Primary Sidebar > Bank > Show All Banks > Edit (row action)`

**Visual Elements:**  
- Bank table  
- Row action controls  
- Edit form

**Step-by-Step Usage:**

1. Open bank list.
2. Select a bank record.
3. Edit and save changes.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Bank permission.
- **Automatic Effects:** Updated details propagate to future linked operations.
- **Constraints:** Tenant scope and field validation rules apply.

**Data Recovery & Cleanup:**  
No dedicated restore page exposed.

**Troubleshooting (Common Blockers):**

- Edit denied if record is out of scope or permission is limited.

**Access Level:**  
Users with bank access permission.

---

### Bank Operations - Bank to Cash

**What it Does:**  
Transfers funds from a bank account into cash.

**Navigation Path:**  
`Primary Sidebar > Bank > Bank to Cash`

**Visual Elements:**  
- Transfer form  
- Bank selector  
- Amount input  
- Submit button

**Step-by-Step Usage:**

1. Open **Bank to Cash**.
2. Choose bank and amount.
3. Submit transfer.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Bank permission and existing bank account.
- **Automatic Effects:** Updates bank and cash ledgers together.
- **Constraints:** Amount must be valid and non-negative.

**Data Recovery & Cleanup:**  
No visible restore flow for transfer records.

**Troubleshooting (Common Blockers):**

- Errors may indicate invalid bank selection or malformed amount.

**Access Level:**  
Users with bank access permission.

---

### Bank Operations - Bank to Bank

**What it Does:**  
Moves funds between two bank accounts.

**Navigation Path:**  
`Primary Sidebar > Bank > Bank to Bank`

**Visual Elements:**  
- Source/destination bank selectors  
- Amount field  
- Submit button

**Step-by-Step Usage:**

1. Open **Bank to Bank**.
2. Select source and destination banks.
3. Enter amount and submit.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Bank permission; at least two usable bank accounts.
- **Automatic Effects:** Posts corresponding debit/credit movements in bank book.
- **Constraints:** Amount and account selections must be valid.

**Data Recovery & Cleanup:**  
No recycle-bin workflow exposed.

**Troubleshooting (Common Blockers):**

- Transfer can fail if same account is selected on both sides or data is incomplete.

**Access Level:**  
Users with bank access permission.

---

### Bank Operations - Bank Book

**What it Does:**  
Provides ledger-style history of bank transactions.

**Navigation Path:**  
`Primary Sidebar > Bank > Bank Book`

**Visual Elements:**  
- Ledger table  
- Date/filter controls  
- Totals area

**Step-by-Step Usage:**

1. Open **Bank Book**.
2. Apply filters/date range.
3. Review entries and balances.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Bank permission.
- **Automatic Effects:** Reflects activity from transfers and related financial workflows.
- **Constraints:** Data appears only for accessible tenant accounts.

**Data Recovery & Cleanup:**  
Report view; no dedicated restore.

**Troubleshooting (Common Blockers):**

- No results usually indicates filter range or no posted activity.

**Access Level:**  
Users with bank access permission.

---

### Supplier Payment - Add Payment

**What it Does:**  
Records payments made to suppliers.

**Navigation Path:**  
`Primary Sidebar > Supplier Payment > Add Payment`

**Visual Elements:**  
- Payment form  
- Supplier selector  
- Amount/date fields  
- Save button

**Step-by-Step Usage:**

1. Open **Add Payment**.
2. Select supplier and payment details.
3. Submit.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Supplier-payment permission.
- **Automatic Effects:** Updates supplier-related financial tracking.
- **Constraints:** Valid supplier linkage and amount/date formatting required.

**Data Recovery & Cleanup:**  
No visible restore/trash menu.

**Troubleshooting (Common Blockers):**

- Submission errors usually indicate incomplete supplier/payment fields.

**Access Level:**  
Users with supplier-payment access permission.

---

### Supplier Payment - Payment List

**What it Does:**  
Shows all supplier payment records for lookup and auditing.

**Navigation Path:**  
`Primary Sidebar > Supplier Payment > Show All Payments`

**Visual Elements:**  
- Payment table  
- Filter/search  
- Row actions

**Step-by-Step Usage:**

1. Open payment list.
2. Search/filter records.
3. Inspect details as needed.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Supplier-payment permission.
- **Automatic Effects:** Tenant-scoped results.
- **Constraints:** Record visibility follows role scope.

**Data Recovery & Cleanup:**  
No public restore flow for deleted entries.

**Troubleshooting (Common Blockers):**

- If records are missing, verify filters and date range.

**Access Level:**  
Users with supplier-payment access permission.

---

### Users Privileges - Add User

**What it Does:**  
Creates tenant team members with controlled access roles.

**Navigation Path:**  
`Primary Sidebar > Users Privileges > Users > Add Users`

**Visual Elements:**  
- User creation form  
- Role selection control  
- Password and confirmation fields  
- Save button

**Step-by-Step Usage:**

1. Open **Add Users**.
2. Fill identity/contact credentials and assign roles.
3. Save new user.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Users-privileges permission.
- **Automatic Effects:** User gains menu visibility according to assigned role permissions.
- **Constraints:** Email must be unique within tenant scope; password minimum length and confirmation required; restricted high-level role assignment is blocked.

**Data Recovery & Cleanup:**  
No dedicated tenant recycle bin for user records shown.

**Troubleshooting (Common Blockers):**

- Duplicate email or password mismatch prevents save.
- Restricted role selection may be rejected for security reasons.

**Access Level:**  
Users with user-privileges management permission.

---

### Users Privileges - User List / Edit User

**What it Does:**  
Lets authorized users review and update tenant user accounts.

**Navigation Path:**  
`Primary Sidebar > Users Privileges > Users > Show All Users > Edit (row action)`

**Visual Elements:**  
- User table  
- Role/status controls  
- Update button

**Step-by-Step Usage:**

1. Open user list.
2. Select a user to edit.
3. Save updates.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Users-privileges permission and edit rights.
- **Automatic Effects:** Updated permissions immediately change available menus/features.
- **Constraints:** Certain protected high-level accounts cannot be modified in tenant flow.

**Data Recovery & Cleanup:**  
No exposed restore path.

**Troubleshooting (Common Blockers):**

- Edit failure may indicate protected account restrictions or invalid role assignment.

**Access Level:**  
Users with user-privileges management permission.

---

### Users Privileges - Add Role

**What it Does:**  
Creates reusable permission bundles for team access control.

**Navigation Path:**  
`Primary Sidebar > Users Privileges > Roles > Add Role`

**Visual Elements:**  
- Role name input  
- Permission checklist/multi-select  
- Save button

**Step-by-Step Usage:**

1. Open **Add Role**.
2. Enter role name and choose permissions.
3. Save role.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Users-privileges permission.
- **Automatic Effects:** New role becomes assignable to users.
- **Constraints:** Role names must be unique within tenant scope; selected permissions must be valid options.

**Data Recovery & Cleanup:**  
No visible role recycle bin.

**Troubleshooting (Common Blockers):**

- Duplicate role names or invalid permission combinations can block save.

**Access Level:**  
Users with user-privileges management permission.

---

### Users Privileges - Role List / Edit Role

**What it Does:**  
Maintains existing roles and their permission sets.

**Navigation Path:**  
`Primary Sidebar > Users Privileges > Roles > Show All Roles > Edit (row action)`

**Visual Elements:**  
- Role table  
- Edit action  
- Permission assignment controls

**Step-by-Step Usage:**

1. Open role list.
2. Choose a role to edit.
3. Update permissions and save.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Users-privileges permission.
- **Automatic Effects:** Role updates impact all users assigned to that role.
- **Constraints:** Role naming and permission validity checks apply.

**Data Recovery & Cleanup:**  
No dedicated restore workflow.

**Troubleshooting (Common Blockers):**

- If updates do not appear, re-check assigned users and refresh session.

**Access Level:**  
Users with user-privileges management permission.

---

### Gate Pass - Gate Pass List

**What it Does:**  
Tracks all gate pass records for movement/dispatch control.

**Navigation Path:**  
`Primary Sidebar > Gate Pass > All Gate Passes`

**Visual Elements:**  
- Door/open icon in sidebar  
- Gate pass table  
- Print action (from row/details)

**Step-by-Step Usage:**

1. Open **All Gate Passes**.
2. Search/review records.
3. Print selected pass if needed.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Gate-pass permission.
- **Automatic Effects:** Shows gate passes linked to tenant records.
- **Constraints:** Access limited by role and tenant scope.

**Data Recovery & Cleanup:**  
No restore/trash menu exposed.

**Troubleshooting (Common Blockers):**

- Missing records can result from insufficient permissions or filter mismatch.

**Access Level:**  
Users with gate-pass access permission.

---

### Gate Pass - Create and Print

**What it Does:**  
Creates printable gate passes from eligible source flows.

**Navigation Path:**  
`Primary Sidebar > Gate Pass > All Gate Passes > Create/Print (context action)`

**Visual Elements:**  
- Create form with name/vehicle/remarks style fields  
- Print-friendly output page  
- Submit and print controls

**Step-by-Step Usage:**

1. Start gate pass creation from eligible context.
2. Complete required details.
3. Save and print.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Gate-pass permission and valid source context.
- **Automatic Effects:** The system may prevent duplicate gate passes and redirect you to an existing printable record.
- **Constraints:** Required fields must be present; duplicate conditions may block new creation.

**Data Recovery & Cleanup:**  
No user-facing restore path.

**Troubleshooting (Common Blockers):**

- If creation fails with a duplicate-style warning, locate and print the existing pass instead.

**Access Level:**  
Users with gate-pass access permission.

---

### Reports - Business Summary

**What it Does:**  
Provides a consolidated business snapshot for selected periods.

**Navigation Path:**  
`Primary Sidebar > Reports > Business Summary`

**Visual Elements:**  
- Reports submenu  
- Summary cards/tables  
- Date-range controls

**Step-by-Step Usage:**

1. Open **Business Summary**.
2. Confirm password when prompted.
3. Select date range and review output.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Reports permission plus password re-confirmation.
- **Automatic Effects:** Pulls aggregated totals from core transactions.
- **Constraints:** Missing baseline account setup can break summary calculations in some environments.

**Data Recovery & Cleanup:**  
Reports are read-only outputs.

**Troubleshooting (Common Blockers):**

- If blocked before opening, complete password confirmation first.
- If data errors appear, verify cash account setup and transaction integrity.

**Access Level:**  
Users with reports permission.

---

### Reports - Profit and Loss

**What it Does:**  
Shows income vs expense performance over time.

**Navigation Path:**  
`Primary Sidebar > Reports > Profit and Loss`

**Visual Elements:**  
- Profit/loss table sections  
- Date filters  
- Total lines

**Step-by-Step Usage:**

1. Open **Profit and Loss**.
2. Confirm password when prompted.
3. Apply period filters and review totals.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Reports permission and password confirmation.
- **Automatic Effects:** Aggregates transaction categories into profit/loss view.
- **Constraints:** Output quality depends on complete transaction posting.

**Data Recovery & Cleanup:**  
Read-only report.

**Troubleshooting (Common Blockers):**

- Inconsistent totals usually trace back to missing or incorrect source transactions.

**Access Level:**  
Users with reports permission.

---

### Reports - Products Reports

**What it Does:**  
Provides product-focused analytical reporting.

**Navigation Path:**  
`Primary Sidebar > Reports > Products Reports`

**Visual Elements:**  
- Product reporting table/chart area  
- Filter controls  
- Export/print patterns (if available)

**Step-by-Step Usage:**

1. Open **Products Reports**.
2. Confirm password if prompted.
3. Filter by product/date and review.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Reports permission and password confirmation.
- **Automatic Effects:** Uses product transaction history for calculations.
- **Constraints:** Limited history yields limited insights.

**Data Recovery & Cleanup:**  
Not applicable.

**Troubleshooting (Common Blockers):**

- Sparse data usually indicates low activity or narrow filter ranges.

**Access Level:**  
Users with reports permission.

---

### Reports - Graphs (Sale/Purchase/Customer/Supplier)

**What it Does:**  
Visualizes trends for key operational dimensions.

**Navigation Path:**  
`Primary Sidebar > Reports > Graphs > [Sale Graph | Purchase Graph | Customer Graph | Supplier Graph]`

**Visual Elements:**  
- Nested Graphs submenu  
- Chart panels  
- Period selectors

**Step-by-Step Usage:**

1. Open a graph type.
2. Confirm password if prompted.
3. Choose timeframe/entity filters and read trend lines.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Reports permission and password confirmation.
- **Automatic Effects:** Fetches chart-ready aggregates based on selected context.
- **Constraints:** Entity-based graphs require valid selected customer/supplier context.

**Data Recovery & Cleanup:**  
Read-only visuals.

**Troubleshooting (Common Blockers):**

- Blank charts usually mean no activity in selected period or missing entity selection.

**Access Level:**  
Users with reports permission.

---

### Settings - Company General

**What it Does:**  
Updates tenant-level company profile details used throughout documents and UI.

**Navigation Path:**  
`Primary Sidebar > Settings > Company > General`

**Visual Elements:**  
- Left settings mini-menu with active item highlight  
- Company detail form  
- Update button

**Step-by-Step Usage:**

1. Open **Settings**.
2. Click **General** under Company.
3. Update details and save.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Settings permission.
- **Automatic Effects:** Updated company data appears in relevant pages/documents.
- **Constraints:** Company name required; optional contact/address fields have length rules; logo upload must be valid image type/size.

**Data Recovery & Cleanup:**  
No explicit version rollback panel exposed.

**Troubleshooting (Common Blockers):**

- Save fails when required company name is missing or logo upload is invalid.

**Access Level:**  
Users with settings access permission.

---

### Settings - Invoice Templates

**What it Does:**  
Lets users choose invoice layout style and preview before applying.

**Navigation Path:**  
`Primary Sidebar > Settings > Company > Invoice Templates`

**Visual Elements:**  
- Invoice template dropdown  
- **Update Invoice Template** button  
- Large **Preview** frame

**Step-by-Step Usage:**

1. Open **Invoice Templates**.
2. Select a template from dropdown.
3. Confirm preview updates.
4. Click update to apply.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Settings permission.
- **Automatic Effects:** Future invoice print pages use selected template style.
- **Constraints:** Template selection is required and must be a valid available template.

**Data Recovery & Cleanup:**  
No recycle-bin concept applies.

**Troubleshooting (Common Blockers):**

- If update fails, reselect a valid template and retry.
- If preview is empty, refresh page and choose template again.

**Access Level:**  
Users with settings access permission.

---

### Profile (Account)

**What it Does:**  
Manages personal account details and profile image.

**Navigation Path:**  
`Header (Top Right Avatar) > Profile`  
or  
`Settings Side Panel > Account > Profile`

**Visual Elements:**  
- Avatar circle in header  
- Profile form  
- Save/update action

**Step-by-Step Usage:**

1. Open Profile from header or account menu.
2. Edit personal details/avatar.
3. Save updates.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Signed-in account.
- **Automatic Effects:** Profile changes reflect in header/user areas.
- **Constraints:** Profile image must meet allowed type/size rules.

**Data Recovery & Cleanup:**  
No restore history shown.

**Troubleshooting (Common Blockers):**

- Image upload errors usually indicate unsupported format or file too large.

**Access Level:**  
Authenticated tenant users.

---

### Change Password (Account Security)

**What it Does:**  
Allows users to update login password securely.

**Navigation Path:**  
`Header (Top Right Avatar) > Change Password`  
or  
`Settings Side Panel > Account > Password`

**Visual Elements:**  
- Old/new/confirm password inputs  
- Save/update button  
- Error message area

**Step-by-Step Usage:**

1. Open password page.
2. Enter current password and new password + confirmation.
3. Submit.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Signed-in account.
- **Automatic Effects:** New password replaces previous login secret.
- **Constraints:** Current password must match; new password must meet minimum length and confirmation requirements.

**Data Recovery & Cleanup:**  
No restore for passwords; reset flow requires standard account recovery path.

**Troubleshooting (Common Blockers):**

- “Current password incorrect” means old password entry does not match.
- “Confirmation mismatch” means new and confirm fields differ.

**Access Level:**  
Authenticated tenant users.

---

### My Subscription

**What it Does:**  
Displays tenant subscription details and status.

**Navigation Path:**  
`Header (Top Right Avatar) > My Subscription`

**Visual Elements:**  
- Subscription page/cards  
- Plan/status dates  
- Expiry-related indicators

**Step-by-Step Usage:**

1. Open avatar menu.
2. Click **My Subscription**.
3. Review current subscription information.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Subscription permission and existing subscription data.
- **Automatic Effects:** Expiry messaging may link users to this page.
- **Constraints:** Page may fail if no subscription record exists.

**Data Recovery & Cleanup:**  
No tenant-side trash/restore concept.

**Troubleshooting (Common Blockers):**

- If page errors or is missing, your role may lack subscription access or no subscription exists yet.

**Access Level:**  
Eligible tenant users with subscription access permission.

---

### Support Messages

**What it Does:**  
Lets users send support requests directly from the app.

**Navigation Path:**  
`Primary Sidebar > Support`

**Visual Elements:**  
- Headset icon in sidebar  
- Subject/message fields  
- Submit button

**Step-by-Step Usage:**

1. Open **Support**.
2. Enter subject and message.
3. Submit request.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Signed-in user access to main app.
- **Automatic Effects:** Message is recorded/sent for support follow-up.
- **Constraints:** Subject and message are required.

**Data Recovery & Cleanup:**  
No tenant-facing message recycle bin identified.

**Troubleshooting (Common Blockers):**

- Submission fails when subject/body is empty.

**Access Level:**  
Tenant users in authenticated workspace.

---

### POS (Direct Feature Access)

**What it Does:**  
Provides point-of-sale transaction entry in a focused layout.

**Navigation Path:**  
`Direct Access Page > POS` (not always shown as a sidebar item)

**Visual Elements:**  
- POS-optimized layout  
- Product/customer/payment controls  
- Transaction action buttons

**Step-by-Step Usage:**

1. Open POS entry page from your enabled shortcut/path.
2. Add items and customer/payment details.
3. Complete sale.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Sales permission.
- **Automatic Effects:** Posts sales and related stock/ledger updates.
- **Constraints:** Same transactional validation principles as standard sale flow.

**Data Recovery & Cleanup:**  
No dedicated restore bin for POS-created sales.

**Troubleshooting (Common Blockers):**

- If POS is unavailable, role may lack sales permission or menu shortcut is disabled in your setup.

**Access Level:**  
Users with sales access permission.

---

### Data Recovery & Cleanup - Platform-Wide Reality Check

**What it Does:**  
Explains how deletion/recovery behaves across modules.

**Navigation Path:**  
`Primary Sidebar > Recovery` (financial recovery only; not trash restore)

**Visual Elements:**  
- Recovery menu for customer payment recovery  
- No global Trash/Recycle Bin menu visible

**Step-by-Step Usage:**

1. Use **Recovery** only for payment recovery workflows.
2. Do not treat it as deleted-record restoration.

**System Rules & Logic (The "Why"):**

- **Prerequisites:** Module-specific permissions.
- **Automatic Effects:** Many deletes are permanent in tenant workflows; some modules may block delete entirely.
- **Constraints:** Restore options are generally not exposed to tenant users.

**Data Recovery & Cleanup:**  
No universal tenant restore center is present in discovered menus/routes.

**Troubleshooting (Common Blockers):**

- If you need a deleted record restored, escalate to system admin/support; in-app self-restore is typically unavailable.

**Access Level:**  
Varies by module permission.
