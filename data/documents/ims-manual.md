# Industrial Management System (IMS) User Manual

This manual explains how the tenant-facing IMS application is used in day-to-day operations. It is written for business users, supervisors, accountants, store staff, and tenant administrators who need to understand what each module does, how to reach it, and what system rules affect their work.

IMS is a permission-based, multi-tenant system. That means the menus, actions, and records available to one user may be hidden or restricted for another user, even within the same company account. Some paths in this guide may also vary slightly depending on whether your role includes create, edit, print, report, or settings permissions.

## How to Use This Manual

- Read the **Overview** first to understand the purpose of a screen or module.
- Use **Navigation Path** to find the feature in the sidebar, header menu, or workflow.
- Follow **Step-by-Step Usage** for the normal user flow.
- Check **How the System Behaves** to understand validations, automatic updates, and access restrictions.
- Use **Troubleshooting** when a page appears blank, a record is missing, or the system blocks an action.

## Important Platform Notes

- Most records are tenant-scoped. You only see data that belongs to your company workspace.
- Many modules do not provide a recycle bin or self-service restore option. Deletions should be treated carefully.
- Reports and dashboards depend on the accuracy of the source transactions. If sales, purchases, recoveries, or expenses are incomplete, reports will also be incomplete.
- Certain pages require prerequisite setup, especially **Terms Acceptance** and **Cash Account Setup**.
- Some sensitive pages, especially report pages, may ask for password confirmation before opening.

## Getting Started

### Terms Acceptance (First Login Gate)

**Overview:**
Ensures users agree to legal terms before using the workspace. This is the first compliance checkpoint after login. Until the terms are accepted, IMS intentionally keeps the rest of the workspace unavailable so legal acceptance is captured before any business activity begins.

**Description:**
This section explains the mandatory terms-acceptance screen that appears before normal workspace access is granted. It is designed to make sure the user has reviewed and accepted the legal or policy requirements of the platform. Until this action is completed successfully, IMS keeps the rest of the application restricted and continues redirecting the user back to the terms page.

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

**How the System Behaves:**
- **Prerequisites:**
You must be signed in.
- **Automatic Effects:**
Accepted status is saved to your profile.
- **Constraints:**
You cannot access core pages until acceptance is complete.

**Data Safety Notes:**
No recycle bin or restore flow applies.

**Troubleshooting:**
- If you keep getting redirected here, acceptance was not saved. Re-submit and refresh.
- If the button does nothing, ensure the consent control is selected.

**Access Level:**
Tenant users who are required to accept terms.

---

### Cash Account Setup (Required Before Regular Use)

**Overview:**
Creates the initial cash account so transactions and ledgers can work correctly. This setup step establishes the opening cash position for the tenant. IMS uses that starting balance as a foundation for later cash movements, books, summaries, and other finance-related screens.

**Description:**
This section explains the first-time cash account setup that must be completed before many day-to-day business modules become usable. The opening cash balance entered here acts as the financial starting point for later cash activity, including transfers, cash books, summaries, and related accounting views. In practical terms, this setup helps IMS understand the tenant's initial cash position before regular transactions begin.

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

**How the System Behaves:**
- **Prerequisites:**
Must be logged in and terms accepted.
- **Automatic Effects:**
Enables normal access to transaction modules.
- **Constraints:**
Opening balance cannot be negative.

**Data Safety Notes:**
No trash/restore path shown for this setup flow.

**Troubleshooting:**
- If redirected repeatedly, setup was not completed successfully.
- If save fails, check that balance is a valid non-negative number.

**Access Level:**
Required for non-admin tenant users before normal module access.

---

### Dashboard Home

**Overview:**
Shows high-level business status and shortcuts to daily work. The dashboard is the operational home page for most users. It is designed to give a quick picture of current business activity and act as the launch point for the modules used most often.

**Description:**
This section describes the main dashboard that users see after successfully entering the tenant workspace. The dashboard is intended to give a quick operational overview of current business activity, surface important metrics or alerts, and act as the central navigation point for the modules a user is allowed to access. It is not just a landing page; it is the main orientation screen for daily work inside IMS.

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

**How the System Behaves:**
- **Prerequisites:**
Account active, terms accepted, cash account ready (for applicable users).
- **Automatic Effects:**
Loads role-based widgets and analytics where permitted.
- **Constraints:**
Some analytics are hidden without analytics permission.

**Data Safety Notes:**
Not applicable.

**Troubleshooting:**
- If analytics panels are missing, your role likely lacks analytics access.
- If login loops, account may be inactive or blocked by prerequisites.

**Access Level:**
Signed-in tenant users; advanced analytics visible only to permitted roles.

---

## Customers and Suppliers

### Customer Management - Add Customer

**Overview:**
Creates customer profiles for sales, ledger tracking, and reporting. This feature should normally be completed before the first sale is recorded for a new customer, so ledger history and receivable tracking begin cleanly from the start.

**Description:**
This section describes how a new customer record is created and why that record matters across the system. A customer profile is more than a name entry; it becomes the basis for future sales, outstanding balances, customer-ledger entries, and reporting visibility. Creating customer records correctly at the start helps keep downstream financial and sales workflows clean and traceable.

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

**How the System Behaves:**
- **Prerequisites:**
Customer permission required.
- **Automatic Effects:**
New customer becomes selectable in sales and ledger screens.
- **Constraints:**
Name length must be valid; opening balance cannot be negative; optional fields still have format/length limits.

**Data Safety Notes:**
No user-facing trash/restore flow for customers.

**Troubleshooting:**
- Save blocked if name is too short/long.
- Invalid phone/address formatting can trigger validation errors.

**Access Level:**
Users with customer access permission.

---

### Customer Management - Customer List

**Overview:**
Displays all customers for review and further actions.

**Description:**
This section describes the customer list as the main review and lookup area for all saved customer records. Users typically come here to search for a customer, confirm whether a record already exists, open the profile for editing, or move into related actions. It serves as the operational index for customer data inside the tenant workspace.

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

**How the System Behaves:**
- **Prerequisites:**
Customer permission required.
- **Automatic Effects:**
List reflects tenant-specific records only.
- **Constraints:**
Cross-tenant records are hidden/restricted.

**Data Safety Notes:**
Deletion restore is not exposed in tenant UI.

**Troubleshooting:**
- If records are missing, confirm you are in the correct tenant workspace.
- If actions are disabled, your role may not include edit privileges.

**Access Level:**
Users with customer access permission.

---

### Customer Management - Edit Customer

**Overview:**
Updates customer details used across transactions and ledgers.

**Description:**
This section explains how an existing customer record can be updated when business information changes or earlier data needs correction. Editing customer details affects how that customer appears in later workflows, documents, and references. Because customer information is reused across multiple modules, keeping it accurate here helps prevent confusion in sales and ledger activity later on.

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

**How the System Behaves:**
- **Prerequisites:**
Customer edit authorization.
- **Automatic Effects:**
Updated details appear in future documents/references.
- **Constraints:**
Same validation rules as creation apply.

**Data Safety Notes:**
No separate version history/restore panel exposed.

**Troubleshooting:**
- Edit denied when record is outside your allowed scope.
- Validation errors occur if updated values break field rules.

**Access Level:**
Users with customer permission and edit rights.

---

### Customer Ledger

**Overview:**
Shows transaction history and balance movement per customer. This screen is primarily for review and reconciliation. It helps users understand how customer balances have changed over time by showing the financial effect of related transactions.

**Description:**
This section describes the customer ledger as a financial history view for a selected customer. It helps users understand how the customer balance has changed over time by showing the entries and movement connected to that account. This is especially useful for reconciliation, follow-up on outstanding balances, and verifying whether posted sales or recoveries are reflected correctly.

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

**How the System Behaves:**
- **Prerequisites:**
Customer permission.
- **Automatic Effects:**
Pulls customer-linked financial entries.
- **Constraints:**
Results depend on existing transaction history.

**Data Safety Notes:**
Ledger is derived from transactions; restore is handled by source transaction policies, not ledger screen.

**Troubleshooting:**
- Empty ledger often means no transactions in selected period.
- If print is blank, adjust filters and retry.

**Access Level:**
Users with customer access permission.

---

### Supplier Management - Add Supplier

**Overview:**
Creates supplier records used in purchases and supplier payments. A well-maintained supplier master record improves purchase entry speed and reduces mistakes in payable tracking and supplier-ledger reporting.

**Description:**
This section explains how to create a supplier record that can later be used in purchases, payments, and supplier-ledger tracking. A supplier profile is a foundational master record inside IMS because many purchasing and payable workflows depend on selecting a valid supplier first. Accurate supplier setup also improves reporting quality and reduces mistakes in future entries.

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

**How the System Behaves:**
- **Prerequisites:**
Supplier permission.
- **Automatic Effects:**
Supplier becomes available in purchase/payment modules.
- **Constraints:**
Name and optional fields must pass length/format checks; opening value cannot be negative.

**Data Safety Notes:**
No visible restore bin for suppliers.

**Troubleshooting:**
- Save fails if required fields are incomplete.
- Invalid phone/address input can block submission.

**Access Level:**
Users with supplier access permission.

---

### Supplier Management - Supplier List / Edit

**Overview:**
Lets users view and maintain supplier records.

**Description:**
This section describes the supplier list and edit flow used to review, search, and maintain supplier records that already exist in the system. It is the place where users confirm supplier details, locate the correct record for a transaction, and update saved information when contact or business details change. In day-to-day use, it serves as the management screen for supplier master data.

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

**How the System Behaves:**
- **Prerequisites:**
Supplier access plus edit authorization.
- **Automatic Effects:**
Updated supplier info flows to future purchasing/payment records.
- **Constraints:**
Tenant scope and validation rules apply.

**Data Safety Notes:**
No tenant-facing restore workflow found.

**Troubleshooting:**
- Edit denied if record is outside your permitted scope.
- Validation errors mirror add-supplier rules.

**Access Level:**
Users with supplier permission and edit rights.

---

### Supplier Ledger

**Overview:**
Provides supplier-side financial history and balances. This module supports supplier reconciliation and payable tracking. It gives teams a timeline of supplier-linked entries so balances can be checked before making new payments or purchases.

**Description:**
This section explains the supplier ledger as the financial history area for a supplier account. It helps users review how balances have moved over time based on supplier-linked transactions, making it easier to understand payables, posted activity, and payment status. This screen is especially valuable when checking what is owed before entering a new payment or purchase.

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

**How the System Behaves:**
- **Prerequisites:**
Supplier permission.
- **Automatic Effects:**
Aggregates supplier-linked transactions.
- **Constraints:**
Requires existing records to display meaningful output.

**Data Safety Notes:**
No recycle bin at ledger level.

**Troubleshooting:**
- No rows usually means no activity in selected range.
- Re-check filters before assuming data loss.

**Access Level:**
Users with supplier access permission.

---

## Products and Inventory

### Product Management - Add Product

**Overview:**
Adds saleable products to catalog and stock workflows. Creating accurate product records helps the sales, stock, and reporting modules stay aligned, especially where pricing and available quantity are important.

**Description:**
This section explains how a saleable product is created in the tenant catalog and why product setup matters across the system. A product record is used not only for display in product lists, but also for stock tracking, sales entry, movement history, and reporting. Well-defined product information improves transaction accuracy and makes later inventory analysis more reliable.

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

**How the System Behaves:**
- **Prerequisites:**
Product permission.
- **Automatic Effects:**
Product appears in sales and inventory-related selections.
- **Constraints:**
Name required; numeric fields cannot be negative; description length limits apply.

**Data Safety Notes:**
No exposed restore/trash path for deleted products.

**Troubleshooting:**
- Submission fails for missing product name.
- Invalid numeric values (negative or non-numeric) block save.

**Access Level:**
Users with product access permission.

---

### Product Management - Product List / Item Flow

**Overview:**
Shows products and movement history for stock tracking.

**Description:**
This section describes the product listing and item-flow view used to manage existing products and review their movement history. The list helps users maintain the product catalog, while the flow view helps them understand how product quantities have changed through operational activity. Together, these screens support both master-data maintenance and stock visibility.

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

**How the System Behaves:**
- **Prerequisites:**
Product permission.
- **Automatic Effects:**
Flow view reflects stock changes from multiple operational areas.
- **Constraints:**
Data visibility remains tenant-scoped.

**Data Safety Notes:**
No dedicated trash module surfaced for product records.

**Troubleshooting:**
- Missing movement lines may be filter-related.
- If item flow is empty for new products, no transactions exist yet.

**Access Level:**
Users with product access permission.

---

### Product Assembly - Create Assembly

**Overview:**
Combines components into assembled products for production workflows. Use this feature when finished goods are created from component or raw items. It helps maintain consistency between stock movement and production-style costing records.

**Description:**
This section explains the assembly workflow used when a finished product is created from component or raw items. Instead of treating the finished item as a simple manual stock adjustment, this feature records the relationship between input items and the assembled result. That makes it useful for businesses that need a clearer production-style view of product creation and costing history.

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

**How the System Behaves:**
- **Prerequisites:**
Assembly permission in addition to base product access patterns.
- **Automatic Effects:**
Assembly records influence product cost/history views.
- **Constraints:**
Component relationships and quantities must be valid.

**Data Safety Notes:**
No dedicated restore bin exposed in UI.

**Troubleshooting:**
- Menu not visible if assembly permission is missing.
- Save errors usually indicate incomplete or inconsistent component setup.

**Access Level:**
Users with product-assembly permission.

---

### Product Assembly - Price History

**Overview:**
Shows historical assembly pricing for audit and costing review.

**Description:**
This section describes the price-history area for assembled products, where users can review earlier assembly-related values over time. It is mainly intended for reference, costing review, and historical comparison rather than direct transaction entry. This helps users understand how assembly pricing or costing has changed across previous operations.

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

**How the System Behaves:**
- **Prerequisites:**
Assembly permission.
- **Automatic Effects:**
History is generated from assembly operations.
- **Constraints:**
Only records with existing assembly history appear.

**Data Safety Notes:**
Historical entries are read-focused; no restore action exposed.

**Troubleshooting:**
- Empty list means no assembly history in selected criteria.

**Access Level:**
Users with product-assembly permission.

---

### Raw Product Management - Add Raw Product

**Overview:**
Creates raw material records used in purchasing and assembly. Raw products are typically used as purchasing and production inputs, so maintaining them properly is important for assembly accuracy and stock visibility.

**Description:**
This section explains how a raw-product record is created for items that are used as inputs rather than final sale products. Raw products are typically referenced during purchasing and assembly processes, so keeping them organized is important for operational accuracy. A properly maintained raw-product master also improves stock clarity in production-oriented workflows.

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

**How the System Behaves:**
- **Prerequisites:**
Raw-product permission.
- **Automatic Effects:**
Raw item becomes selectable in purchase/assembly flows.
- **Constraints:**
Standard field validation and tenant-scoping apply.

**Data Safety Notes:**
No tenant trash/restore page surfaced.

**Troubleshooting:**
- Save blocked by missing required fields or invalid formats.

**Access Level:**
Users with raw-product access permission.

---

### Raw Product Management - Raw Product List

**Overview:**
Displays all raw material records for maintenance and lookup.

**Description:**
This section describes the raw-product list as the main page for reviewing and maintaining all raw-material records saved for the tenant. Users can use it to confirm whether an item already exists, browse current records, and open available actions for maintenance. It functions as the management screen for raw-material master data.

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

**How the System Behaves:**
- **Prerequisites:**
Raw-product permission.
- **Automatic Effects:**
Tenant-specific records only.
- **Constraints:**
Cross-tenant records are not accessible.

**Data Safety Notes:**
No dedicated recovery/trash route exposed.

**Troubleshooting:**
- If expected items are absent, verify workspace/tenant and filters.

**Access Level:**
Users with raw-product access permission.

---

## Purchasing and Sales

### Purchase Workflow - Create Purchase

**Overview:**
Records incoming stock from suppliers. A purchase entry does more than save a document. It usually affects stock quantities, supplier-facing balances, and downstream financial reporting.

**Description:**
This section explains the purchase-entry workflow used to record incoming goods from suppliers. A purchase transaction usually does more than save a document: it can update stock, affect supplier-facing balances, and feed future reports and ledger views. Because of that, purchase creation is one of the central operational processes in IMS.

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

**How the System Behaves:**
- **Prerequisites:**
Purchase permission.
- **Automatic Effects:**
Updates stock and financial records connected to purchase workflows.
- **Constraints:**
Required fields and valid numeric values are mandatory.

**Data Safety Notes:**
No general restore bin for deleted purchases.

**Troubleshooting:**
- Wrong branch selection (raw vs sale product purchase) causes mismatched item context.
- Save failures usually indicate missing supplier/items or invalid totals.

**Access Level:**
Users with purchase access permission.

---

### Purchase Workflow - Purchase List

**Overview:**
Shows recorded purchases for review, print, and lifecycle actions.

**Description:**
This section describes the purchase list as the review area for previously recorded purchases. Users use it to search historical transactions, verify what has already been posted, open available row-level actions, and locate records for printing or follow-up. It acts as the main audit and lookup screen for purchase activity.

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

**How the System Behaves:**
- **Prerequisites:**
Purchase permission.
- **Automatic Effects:**
List reflects tenant and purchase-type context.
- **Constraints:**
Cross-tenant records are restricted.

**Data Safety Notes:**
Deleted purchase records do not expose a standard restore menu.

**Troubleshooting:**
- If expected purchase is missing, verify purchase-type branch and date filters.

**Access Level:**
Users with purchase access permission.

---

### Purchase Workflow - Print Purchase Document

**Overview:**
Generates a print-friendly purchase document.

**Description:**
This section explains the print flow for an existing purchase document. Its purpose is to provide a clean, print-friendly version of the transaction that can be used for internal records, supplier communication, or physical documentation. It is a document-output step rather than a data-entry step.

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

**How the System Behaves:**
- **Prerequisites:**
Purchase record must exist and be accessible.
- **Automatic Effects:**
No data changes; output only.
- **Constraints:**
Inaccessible records cannot be printed.

**Data Safety Notes:**
Not applicable.

**Troubleshooting:**
- Print fails if record was deleted or outside your authorization scope.

**Access Level:**
Users with purchase access permission.

---

### Purchase Return - Create Return

**Overview:**
Records items returned against prior purchases. Returns should usually be recorded against the correct source purchase so item movement and supplier-side balances stay traceable and auditable.

**Description:**
This section explains how to record a return against an earlier purchase transaction when goods need to be sent back. The return process helps maintain accurate stock and supplier-related financial tracking by explicitly linking the returned items to the original purchase context. It is important for keeping both quantity movement and financial history consistent.

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

**How the System Behaves:**
- **Prerequisites:**
Purchase permission and valid source purchase.
- **Automatic Effects:**
Adjusts stock/financial impact per return workflow.
- **Constraints:**
Returned items must match selected purchase context.

**Data Safety Notes:**
No dedicated restore bin found for purchase returns.

**Troubleshooting:**
- Return item list may stay empty if source purchase is not selected/valid.
- Submission errors often indicate invalid item mapping or quantities.

**Access Level:**
Users with purchase access permission.

---

### Purchase Return - Return List

**Overview:**
Shows all purchase return entries for tracking and review.

**Description:**
This section describes the list of recorded purchase returns that users can review after return entries have been posted. It helps with verification, historical lookup, and understanding what return activity has already been captured in the system. In practice, it serves as the reference page for purchase-return history.

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

**How the System Behaves:**
- **Prerequisites:**
Purchase permission.
- **Automatic Effects:**
Data remains branch-specific by purchase type.
- **Constraints:**
Tenant-scope restrictions apply.

**Data Safety Notes:**
No visible restore flow for return deletions.

**Troubleshooting:**
- If data appears incomplete, verify branch, date, and supplier filters.

**Access Level:**
Users with purchase access permission.

---

### Sales Workflow - Add Sale

**Overview:**
Creates sales transactions and invoice-ready customer billing records. A sale is one of the most important operational transactions in IMS. Posting it can affect customer balances, stock movement, dashboards, and reports at the same time.

**Description:**
This section explains the primary sales-entry workflow used to record a customer sale in IMS. Posting a sale can affect several areas at once, including stock levels, customer balances, dashboards, and later reports. Because of that, the sale form is one of the most important transaction screens in the entire application.

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

**How the System Behaves:**
- **Prerequisites:**
Sales permission and valid products/customers.
- **Automatic Effects:**
Updates stock and financial ledgers based on sale.
- **Constraints:**
Invalid quantities or incomplete required fields block submission.

**Data Safety Notes:**
No standard restore bin for deleted sales.

**Troubleshooting:**
- Submission failures often come from incomplete item/payment details.
- If stock-linked errors appear, review quantities and item availability.

**Access Level:**
Users with sales access permission.

---

### Sales Workflow - Sales List

**Overview:**
Displays all sales with access to review and further actions.

**Description:**
This section describes the sales list as the main history and review page for posted sales. Users come here to search for older sales, verify what has been entered, and access allowed actions such as printing or deletion where permissions permit. It is the central lookup area for sales activity already stored in the system.

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

**How the System Behaves:**
- **Prerequisites:**
Sales permission.
- **Automatic Effects:**
Shows tenant-scoped records only.
- **Constraints:**
Hidden/blocked actions depend on permissions and record state.

**Data Safety Notes:**
Deleted sales do not expose tenant restore screens.

**Troubleshooting:**
- Missing rows are often due to filters or tenant context mismatch.

**Access Level:**
Users with sales access permission.

---

### Sales Workflow - Print Sale Invoice

**Overview:**
Creates printable customer invoices using your selected invoice template style.

**Description:**
This section explains how an existing sale is turned into a printable invoice output. The page is mainly intended for producing a customer-facing document that can be printed, saved, or shared as part of the sales process. It focuses on formal presentation of the recorded sale rather than editing the transaction itself.

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

**How the System Behaves:**
- **Prerequisites:**
Sales record exists and is accessible.
- **Automatic Effects:**
Uses your current invoice template preference for visual format.
- **Constraints:**
If template setting is missing/invalid, output may fallback or fail visually.

**Data Safety Notes:**
Not applicable.

**Troubleshooting:**
- Unexpected invoice look: verify selected template under Settings > Invoice Templates.

**Access Level:**
Users with sales access permission.

---

### Sales Return - Add Sale Return

**Overview:**
Processes customer returns against original sales. This screen is used to formally reverse or adjust earlier sale activity where goods are returned after the original invoice has been posted.

**Description:**
This section explains the workflow for recording returned goods after a sale has already been posted. It helps reverse or adjust the original sale in a traceable manner so stock movement and customer-facing financial effects remain accurate. This is especially important when businesses need a formal record of returned items instead of making informal adjustments.

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

**How the System Behaves:**
- **Prerequisites:**
Sales permission and valid source sale.
- **Automatic Effects:**
Adjusts stock and return-related financial impact.
- **Constraints:**
Return items must map to source sale context.

**Data Safety Notes:**
No dedicated restore bin surfaced for sale returns.

**Troubleshooting:**
- Empty return items usually means source sale is not selected or not eligible.

**Access Level:**
Users with sales access permission.

---

### Sales Return - Return List

**Overview:**
Shows all sales return transactions for tracking and audit.

**Description:**
This section describes the list of recorded sales returns that have already been saved in the system. It helps users review return history, verify what has been posted, and confirm whether a return has already been handled. It acts as the historical reference page for sale-return activity.

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

**How the System Behaves:**
- **Prerequisites:**
Sales permission.
- **Automatic Effects:**
Data is tenant-scoped.
- **Constraints:**
Records outside your scope are hidden/blocked.

**Data Safety Notes:**
No user-facing restore workflow found.

**Troubleshooting:**
- Missing records are commonly filter-related.

**Access Level:**
Users with sales access permission.

---

## Recoveries, Expenses, Cash, and Banking

### Customer Recovery - Add Recovery Entry

**Overview:**
Records customer payment recovery activity (not a recycle bin function). This workflow is intended for incoming customer payments or balance settlements rather than generic note-taking, so it should be entered carefully and against the correct customer.

**Description:**
This section explains the customer recovery workflow used to record money received from a customer against their pending balance. In IMS, "recovery" refers to payment collection and settlement activity, not restoration of deleted records. This screen is important for keeping receivable tracking accurate and for showing that customer balances have been reduced properly.

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

**How the System Behaves:**
- **Prerequisites:**
Recovery permission.
- **Automatic Effects:**
Updates customer financial tracking.
- **Constraints:**
Amount/date and linked data must be valid.

**Data Safety Notes:**
This module is financial recovery; it is not a deleted-item restore area.

**Troubleshooting:**
- If customer-specific history is missing, verify selected customer and prior transactions.

**Access Level:**
Users with recovery access permission.

---

### Customer Recovery - Recovery List

**Overview:**
Lists all customer recovery entries for review.

**Description:**
This section describes the list of customer recovery entries already posted in the system. It helps users review payment-recovery history, verify collected amounts, and reconcile what has been received from customers over time. It is the historical reference view for customer-settlement activity.

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

**How the System Behaves:**
- **Prerequisites:**
Recovery permission.
- **Automatic Effects:**
Reflects tenant-specific recovery records.
- **Constraints:**
Scope and record-level permissions apply.

**Data Safety Notes:**
No restore bin for deleted recovery records was surfaced.

**Troubleshooting:**
- Empty results are typically date/filter selection issues.

**Access Level:**
Users with recovery access permission.

---

### Expense Management - Add New Expense

**Overview:**
Captures business expenses with category/type tracking. Expense posting helps keep profitability and cash visibility realistic, so it should be recorded consistently and with the correct expense classification.

**Description:**
This section explains how to record a business expense using the correct type, name, amount, and supporting details. Expense entries matter because they feed cash movement, financial tracking, and profitability-related reports. Accurate expense posting helps make reports and summaries reflect the real cost of operating the business.

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

**How the System Behaves:**
- **Prerequisites:**
Expense permission.
- **Automatic Effects:**
Posts expense to financial records.
- **Constraints:**
Amount must be non-negative; date format must be valid; selected expense name must belong to selected expense type; optional bank must belong to your tenant workspace; notes length has a limit.

**Data Safety Notes:**
No user-facing restore bin for deleted expenses.

**Troubleshooting:**
- Mismatch between expense type and expense name is a common error.
- Invalid date format blocks submission.

**Access Level:**
Users with expense access permission.

---

### Expense Management - Expense List

**Overview:**
Displays historical expense records for auditing and updates.

**Description:**
This section describes the expense list as the review page for previously recorded expenses. Users can use it to inspect historical expense activity, check posted amounts, and verify whether entries appear correctly under the expected categories. It functions as the main lookup and audit screen for tenant expense records.

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

**How the System Behaves:**
- **Prerequisites:**
Expense permission.
- **Automatic Effects:**
Tenant-only records are shown.
- **Constraints:**
Visibility follows role and tenant scope.

**Data Safety Notes:**
No restore/trash page surfaced for expense records.

**Troubleshooting:**
- If records appear missing, verify filters and date range.

**Access Level:**
Users with expense access permission.

---

### Cash Operations - Cash Account Page

**Overview:**
Maintains ongoing cash account settings and opening/working balances. This page is the primary maintenance point for the tenant cash account and is often used as a reference before transfers, books, and summary checks.

**Description:**
This section explains the cash account page as the central maintenance and reference screen for tenant cash settings. It gives users a place to review the current configured cash position and update allowed values where necessary. Since many financial workflows rely on the cash account, this page plays an important supporting role in the system.

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

**How the System Behaves:**
- **Prerequisites:**
Cash permission and existing cash account.
- **Automatic Effects:**
Changes affect downstream cash-based reports/flows.
- **Constraints:**
Numeric constraints apply to cash values.

**Data Safety Notes:**
No dedicated restore history in UI.

**Troubleshooting:**
- If inaccessible, ensure initial cash setup was completed and role includes cash access.

**Access Level:**
Users with cash access permission.

---

### Cash Operations - Cash to Bank Transfer

**Overview:**
Moves funds from cash account into a selected bank account.

**Description:**
This section explains the workflow used to transfer funds from the tenant cash account into a selected bank account. It exists so the movement is recorded formally rather than handled as an informal adjustment. By posting the transfer through this screen, IMS can keep both cash-side and bank-side history aligned.

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

**How the System Behaves:**
- **Prerequisites:**
Cash permission; bank records available.
- **Automatic Effects:**
Updates both cash and bank books.
- **Constraints:**
Transfer amounts must be valid and non-negative.

**Data Safety Notes:**
No end-user restore flow for transfer deletions.

**Troubleshooting:**
- Transfer errors may occur if bank selection is invalid or amount is malformed.

**Access Level:**
Users with cash access permission.

---

### Cash Operations - Cash Book

**Overview:**
Shows chronological cash movements for reconciliation. The cash book is typically used by accountants and supervisors to verify that daily inflows and outflows match expected business activity.

**Description:**
This section describes the cash book as the running history of cash-related movements within the tenant workspace. It helps users review inflows, outflows, and other cash-side changes over time so they can reconcile activity and confirm expected balances. This page is especially useful for finance-focused review and daily checking.

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

**How the System Behaves:**
- **Prerequisites:**
Cash permission.
- **Automatic Effects:**
Pulls transaction-linked cash movements.
- **Constraints:**
Output depends on existing transactions and selected range.

**Data Safety Notes:**
Derived report; no separate restore flow.

**Troubleshooting:**
- Empty report often means no transactions in selected period.

**Access Level:**
Users with cash access permission.

---

### Bank Operations - Add New Bank

**Overview:**
Creates bank accounts for transfers and ledger tracking. Bank records support transfer workflows, bank books, and formal accounting visibility for non-cash balances.

**Description:**
This section explains how a bank record is created inside the tenant workspace so that bank-related workflows can be used correctly. Without valid bank records, transfer pages and bank books have no proper account context to work with. In practical terms, this setup step prepares the system for formal bank-side transaction tracking.

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

**How the System Behaves:**
- **Prerequisites:**
Bank permission.
- **Automatic Effects:**
New bank becomes available in transfer and expense flows.
- **Constraints:**
Account number must be unique; opening values cannot be negative.

**Data Safety Notes:**
No visible restore/trash flow for bank accounts.

**Troubleshooting:**
- Duplicate account number blocks submission.

**Access Level:**
Users with bank access permission.

---

### Bank Operations - Show All Banks / Edit Bank

**Overview:**
Lists bank accounts and allows bank record updates.

**Description:**
This section describes the page used to review and maintain bank records that have already been created. Users can search existing bank entries, confirm account details, and update saved information when necessary. It serves as the management area for tenant bank master data.

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

**How the System Behaves:**
- **Prerequisites:**
Bank permission.
- **Automatic Effects:**
Updated details propagate to future linked operations.
- **Constraints:**
Tenant scope and field validation rules apply.

**Data Safety Notes:**
No dedicated restore page exposed.

**Troubleshooting:**
- Edit denied if record is out of scope or permission is limited.

**Access Level:**
Users with bank access permission.

---

### Bank Operations - Bank to Cash

**Overview:**
Transfers funds from a bank account into cash.

**Description:**
This section explains the transfer flow used when funds move from a bank account into cash. It helps record the withdrawal or reclassification in a structured way so both financial sides of the movement remain visible in system history. This is important for keeping books and balances internally consistent.

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

**How the System Behaves:**
- **Prerequisites:**
Bank permission and existing bank account.
- **Automatic Effects:**
Updates bank and cash ledgers together.
- **Constraints:**
Amount must be valid and non-negative.

**Data Safety Notes:**
No visible restore flow for transfer records.

**Troubleshooting:**
- Errors may indicate invalid bank selection or malformed amount.

**Access Level:**
Users with bank access permission.

---

### Bank Operations - Bank to Bank

**Overview:**
Moves funds between two bank accounts.

**Description:**
This section explains the workflow for transferring money from one saved bank account to another. It ensures that the movement is captured against both the source and destination account instead of being treated like an untracked adjustment. This improves traceability and keeps bank histories more accurate.

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

**How the System Behaves:**
- **Prerequisites:**
Bank permission; at least two usable bank accounts.
- **Automatic Effects:**
Posts corresponding debit/credit movements in bank book.
- **Constraints:**
Amount and account selections must be valid.

**Data Safety Notes:**
No recycle-bin workflow exposed.

**Troubleshooting:**
- Transfer can fail if same account is selected on both sides or data is incomplete.

**Access Level:**
Users with bank access permission.

---

### Bank Operations - Bank Book

**Overview:**
Provides ledger-style history of bank transactions. The bank book provides a review-focused history of bank-side movement, helping users match internal records against statements or transfer activity.

**Description:**
This section describes the bank book as the running history of transactions connected to bank accounts. Users commonly rely on it to review movement, verify transfer postings, and compare internal records with external bank statements. It functions as the main reporting-style view for bank-side activity.

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

**How the System Behaves:**
- **Prerequisites:**
Bank permission.
- **Automatic Effects:**
Reflects activity from transfers and related financial workflows.
- **Constraints:**
Data appears only for accessible tenant accounts.

**Data Safety Notes:**
Report view; no dedicated restore.

**Troubleshooting:**
- No results usually indicates filter range or no posted activity.

**Access Level:**
Users with bank access permission.

---

### Supplier Payment - Add Payment

**Overview:**
Records payments made to suppliers. This entry should be posted against the correct supplier so balances, ledgers, and historical payment records remain accurate.

**Description:**
This section explains how to record a payment made to a supplier so that the payable side of the system remains accurate. Posting the payment here helps IMS reflect the reduction in what is owed and keeps supplier-ledger history aligned with real business activity. It is an important follow-up workflow after purchases have been posted.

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

**How the System Behaves:**
- **Prerequisites:**
Supplier-payment permission.
- **Automatic Effects:**
Updates supplier-related financial tracking.
- **Constraints:**
Valid supplier linkage and amount/date formatting required.

**Data Safety Notes:**
No visible restore/trash menu.

**Troubleshooting:**
- Submission errors usually indicate incomplete supplier/payment fields.

**Access Level:**
Users with supplier-payment access permission.

---

### Supplier Payment - Payment List

**Overview:**
Shows all supplier payment records for lookup and auditing.

**Description:**
This section describes the supplier-payment list as the review page for payments that have already been entered. Users can use it to verify payment history, inspect amounts and dates, and confirm whether supplier settlements have been recorded correctly. It serves as the reference area for supplier-payment activity.

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

**How the System Behaves:**
- **Prerequisites:**
Supplier-payment permission.
- **Automatic Effects:**
Tenant-scoped results.
- **Constraints:**
Record visibility follows role scope.

**Data Safety Notes:**
No public restore flow for deleted entries.

**Troubleshooting:**
- If records are missing, verify filters and date range.

**Access Level:**
Users with supplier-payment access permission.

---

## Users, Roles, and Administration

### Users Privileges - Add User

**Overview:**
Creates tenant team members with controlled access roles. This is one of the most sensitive tenant administration tasks because the new account immediately affects who can see menus, create records, or access financial data.

**Description:**
This section explains the tenant user-creation workflow used to add another person to the workspace. When a new user is created, their assigned role determines which menus, records, and actions become available to them. Because of that, this page is not just for identity creation; it is also a key access-control step.

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

**How the System Behaves:**
- **Prerequisites:**
Users-privileges permission.
- **Automatic Effects:**
User gains menu visibility according to assigned role permissions.
- **Constraints:**
Email must be unique within tenant scope; password minimum length and confirmation required; restricted high-level role assignment is blocked.

**Data Safety Notes:**
No dedicated tenant recycle bin for user records shown.

**Troubleshooting:**
- Duplicate email or password mismatch prevents save.
- Restricted role selection may be rejected for security reasons.

**Access Level:**
Users with user-privileges management permission.

---

### Users Privileges - User List / Edit User

**Overview:**
Lets authorized users review and update tenant user accounts.

**Description:**
This section describes the page used to review and maintain existing tenant user accounts. Administrators or authorized staff can use it to update saved details, change role assignments, and manage user-level access behaviour. It acts as the main maintenance screen for tenant users after they have been created.

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

**How the System Behaves:**
- **Prerequisites:**
Users-privileges permission and edit rights.
- **Automatic Effects:**
Updated permissions immediately change available menus/features.
- **Constraints:**
Certain protected high-level accounts cannot be modified in tenant flow.

**Data Safety Notes:**
No exposed restore path.

**Troubleshooting:**
- Edit failure may indicate protected account restrictions or invalid role assignment.

**Access Level:**
Users with user-privileges management permission.

---

### Users Privileges - Add Role

**Overview:**
Creates reusable permission bundles for team access control. Roles are the main way to standardize access across a tenant team. A well-designed role structure reduces mistakes and keeps menus aligned with real job responsibilities.

**Description:**
This section explains how to create a reusable role that groups permissions together for easier access management. Instead of assigning permissions individually every time, teams can define standard role patterns and reuse them across multiple users. This makes access control cleaner, faster, and easier to manage at scale.

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

**How the System Behaves:**
- **Prerequisites:**
Users-privileges permission.
- **Automatic Effects:**
New role becomes assignable to users.
- **Constraints:**
Role names must be unique within tenant scope; selected permissions must be valid options.

**Data Safety Notes:**
No visible role recycle bin.

**Troubleshooting:**
- Duplicate role names or invalid permission combinations can block save.

**Access Level:**
Users with user-privileges management permission.

---

### Users Privileges - Role List / Edit Role

**Overview:**
Maintains existing roles and their permission sets.

**Description:**
This section describes the role-management page used to review and update existing permission roles. Editing a role can have broad effects because the change may apply to every user currently assigned to that role. For that reason, this screen is important for long-term tenant access governance.

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

**How the System Behaves:**
- **Prerequisites:**
Users-privileges permission.
- **Automatic Effects:**
Role updates impact all users assigned to that role.
- **Constraints:**
Role naming and permission validity checks apply.

**Data Safety Notes:**
No dedicated restore workflow.

**Troubleshooting:**
- If updates do not appear, re-check assigned users and refresh session.

**Access Level:**
Users with user-privileges management permission.

---

### Gate Pass - Gate Pass List

**Overview:**
Tracks all gate pass records for movement/dispatch control.

**Description:**
This section explains the list of gate pass records used to review movement-related documents that have already been created. Users can search for a pass, inspect what exists, and locate records that may need to be printed again. It serves as the historical and operational lookup page for gate-pass activity.

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

**How the System Behaves:**
- **Prerequisites:**
Gate-pass permission.
- **Automatic Effects:**
Shows gate passes linked to tenant records.
- **Constraints:**
Access limited by role and tenant scope.

**Data Safety Notes:**
No restore/trash menu exposed.

**Troubleshooting:**
- Missing records can result from insufficient permissions or filter mismatch.

**Access Level:**
Users with gate-pass access permission.

---

### Gate Pass - Create and Print

**Overview:**
Creates printable gate passes from eligible source flows. Gate passes are operational control documents, so the goal is usually both record creation and immediate print readiness for dispatch or movement verification.

**Description:**
This section explains the workflow for creating a gate pass and preparing it for immediate printing. It is typically used in dispatch, movement control, or operational verification scenarios where a document needs to accompany goods or movement activity. The screen therefore supports both record creation and practical document output.

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

**How the System Behaves:**
- **Prerequisites:**
Gate-pass permission and valid source context.
- **Automatic Effects:**
The system may prevent duplicate gate passes and redirect you to an existing printable record.
- **Constraints:**
Required fields must be present; duplicate conditions may block new creation.

**Data Safety Notes:**
No user-facing restore path.

**Troubleshooting:**
- If creation fails with a duplicate-style warning, locate and print the existing pass instead.

**Access Level:**
Users with gate-pass access permission.

---

## Reports and Insights

### Reports - Business Summary

**Overview:**
Provides a consolidated business snapshot for selected periods. This report gives management a broad snapshot rather than a transaction-by-transaction view. It is most useful after routine data entry has been completed accurately.

**Description:**
This section describes the business-summary report that gives management or supervisors a consolidated snapshot of business performance for a selected period. Instead of focusing on one single transaction type, it pulls together high-level information from core activity across the tenant workspace. It is mainly intended for summary-level review and decision support.

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

**How the System Behaves:**
- **Prerequisites:**
Reports permission plus password re-confirmation.
- **Automatic Effects:**
Pulls aggregated totals from core transactions.
- **Constraints:**
Missing baseline account setup can break summary calculations in some environments.

**Data Safety Notes:**
Reports are read-only outputs.

**Troubleshooting:**
- If blocked before opening, complete password confirmation first.
- If data errors appear, verify cash account setup and transaction integrity.

**Access Level:**
Users with reports permission.

---

### Reports - Profit and Loss

**Overview:**
Shows income vs expense performance over time. This is a management-facing report and is only as reliable as the transactions already posted in sales, purchases, expenses, and related financial workflows.

**Description:**
This section explains the profit-and-loss report that compares income and expenses over a selected period. It helps users understand whether operations are producing a positive or negative financial outcome based on the transactions already posted in the system. This report is especially useful for management review and financial performance analysis.

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

**How the System Behaves:**
- **Prerequisites:**
Reports permission and password confirmation.
- **Automatic Effects:**
Aggregates transaction categories into profit/loss view.
- **Constraints:**
Output quality depends on complete transaction posting.

**Data Safety Notes:**
Read-only report.

**Troubleshooting:**
- Inconsistent totals usually trace back to missing or incorrect source transactions.

**Access Level:**
Users with reports permission.

---

### Reports - Products Reports

**Overview:**
Provides product-focused analytical reporting.

**Description:**
This section describes the product-focused reporting area used to analyze activity connected to products over time. It helps users move beyond basic transaction entry and look at product-level behaviour, trends, and outcomes in a more analytical way. This makes it valuable for planning, review, and operational decision-making.

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

**How the System Behaves:**
- **Prerequisites:**
Reports permission and password confirmation.
- **Automatic Effects:**
Uses product transaction history for calculations.
- **Constraints:**
Limited history yields limited insights.

**Data Safety Notes:**
Not applicable.

**Troubleshooting:**
- Sparse data usually indicates low activity or narrow filter ranges.

**Access Level:**
Users with reports permission.

---

### Reports - Graphs (Sale/Purchase/Customer/Supplier)

**Overview:**
Visualizes trends for key operational dimensions.

**Description:**
This section explains the graph-based reporting area that turns transaction data into visual trend displays. Instead of reading only tables and totals, users can quickly compare patterns through charts focused on sales, purchases, customers, or suppliers. This is especially helpful for spotting movement trends and changes across time periods.

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

**How the System Behaves:**
- **Prerequisites:**
Reports permission and password confirmation.
- **Automatic Effects:**
Fetches chart-ready aggregates based on selected context.
- **Constraints:**
Entity-based graphs require valid selected customer/supplier context.

**Data Safety Notes:**
Read-only visuals.

**Troubleshooting:**
- Blank charts usually mean no activity in selected period or missing entity selection.

**Access Level:**
Users with reports permission.

---

## Settings and Personal Account

### Settings - Company General

**Overview:**
Updates tenant-level company profile details used throughout documents and UI. These company details are reused across the system, especially in printed documents, headers, and business identity references.

**Description:**
This section describes the company-general settings page where tenant-level business identity information is maintained. These details can appear in printed documents, interface areas, and other system-generated outputs, so they should be kept current and accurate. This page is about organization-level profile settings, not personal account information.

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

**How the System Behaves:**
- **Prerequisites:**
Settings permission.
- **Automatic Effects:**
Updated company data appears in relevant pages/documents.
- **Constraints:**
Company name required; optional contact/address fields have length rules; logo upload must be valid image type/size.

**Data Safety Notes:**
No explicit version rollback panel exposed.

**Troubleshooting:**
- Save fails when required company name is missing or logo upload is invalid.

**Access Level:**
Users with settings access permission.

---

### Settings - Invoice Templates

**Overview:**
Lets users choose invoice layout style and preview before applying. Choosing the right template helps keep printed invoices consistent with the company?s preferred presentation style.

**Description:**
This section explains the invoice-template settings area where the tenant chooses which invoice design should be used for printed outputs. It helps standardize the visual presentation of invoices and supports businesses that want a preferred document style. This setting affects the appearance of future invoice print pages rather than the underlying transaction data.

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

**How the System Behaves:**
- **Prerequisites:**
Settings permission.
- **Automatic Effects:**
Future invoice print pages use selected template style.
- **Constraints:**
Template selection is required and must be a valid available template.

**Data Safety Notes:**
No recycle-bin concept applies.

**Troubleshooting:**
- If update fails, reselect a valid template and retry.
- If preview is empty, refresh page and choose template again.

**Access Level:**
Users with settings access permission.

---

### Profile (Account)

**Overview:**
Manages personal account details and profile image. This page affects the signed-in user?s own identity details rather than tenant-wide company settings.

**Description:**
This section describes the personal profile page for the currently signed-in user. It is used to maintain individual account details such as identity information and profile image where supported. Unlike company settings, this page affects the user's own account presence rather than tenant-wide business configuration.

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

**How the System Behaves:**
- **Prerequisites:**
Signed-in account.
- **Automatic Effects:**
Profile changes reflect in header/user areas.
- **Constraints:**
Profile image must meet allowed type/size rules.

**Data Safety Notes:**
No restore history shown.

**Troubleshooting:**
- Image upload errors usually indicate unsupported format or file too large.

**Access Level:**
Authenticated tenant users.

---

### Change Password (Account Security)

**Overview:**
Allows users to update login password securely. Use this feature whenever credentials need to be refreshed for security or handed over from a temporary setup password to a personal one.

**Description:**
This section explains the password-change page used to replace the current login password with a new one. It is intended for account security maintenance and is especially useful when users want to strengthen credentials or move away from an initial shared or temporary password. This workflow updates the authentication secret for the signed-in account.

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

**How the System Behaves:**
- **Prerequisites:**
Signed-in account.
- **Automatic Effects:**
New password replaces previous login secret.
- **Constraints:**
Current password must match; new password must meet minimum length and confirmation requirements.

**Data Safety Notes:**
No restore for passwords; reset flow requires standard account recovery path.

**Troubleshooting:**
- “Current password incorrect” means old password entry does not match.
- “Confirmation mismatch” means new and confirm fields differ.

**Access Level:**
Authenticated tenant users.

---

### My Subscription

**Overview:**
Displays tenant subscription details and status. This page is mainly informational and helps users understand plan status, expiry timing, and subscription-related availability.

**Description:**
This section describes the subscription page that shows the tenant's current subscription-related information. It helps users understand plan status, expiry timing, and whether subscription visibility or warnings relate to their account state. This screen is informational in nature and supports awareness rather than transaction entry.

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

**How the System Behaves:**
- **Prerequisites:**
Subscription permission and existing subscription data.
- **Automatic Effects:**
Expiry messaging may link users to this page.
- **Constraints:**
Page may fail if no subscription record exists.

**Data Safety Notes:**
No tenant-side trash/restore concept.

**Troubleshooting:**
- If page errors or is missing, your role may lack subscription access or no subscription exists yet.

**Access Level:**
Eligible tenant users with subscription access permission.

---

### Support Messages

**Overview:**
Lets users send support requests directly from the app. This is the built-in channel for sending structured support requests without leaving the IMS workspace.

**Description:**
This section explains the in-application support messaging feature that lets users send help or support requests without leaving IMS. It acts as a structured communication channel where users can describe an issue or request assistance directly from the tenant workspace. This is helpful for operational support and issue reporting.

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

**How the System Behaves:**
- **Prerequisites:**
Signed-in user access to main app.
- **Automatic Effects:**
Message is recorded/sent for support follow-up.
- **Constraints:**
Subject and message are required.

**Data Safety Notes:**
No tenant-facing message recycle bin identified.

**Troubleshooting:**
- Submission fails when subject/body is empty.

**Access Level:**
Tenant users in authenticated workspace.

---

### POS (Direct Feature Access)

**Overview:**
Provides point-of-sale transaction entry in a focused layout. The POS screen is designed for faster transaction entry in live selling environments where speed and clarity matter more than full back-office navigation.

**Description:**
This section describes the focused point-of-sale screen designed for faster, more direct sale entry. It is generally used in selling scenarios where speed, simplicity, and quick transaction completion matter more than full back-office navigation. Although streamlined, it still participates in the same broader sales and stock logic as standard sale workflows.

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

**How the System Behaves:**
- **Prerequisites:**
Sales permission.
- **Automatic Effects:**
Posts sales and related stock/ledger updates.
- **Constraints:**
Same transactional validation principles as standard sale flow.

**Data Safety Notes:**
No dedicated restore bin for POS-created sales.

**Troubleshooting:**
- If POS is unavailable, role may lack sales permission or menu shortcut is disabled in your setup.

**Access Level:**
Users with sales access permission.

---

## Platform Behaviour and Data Safety

### Data Recovery & Cleanup - Platform-Wide Reality Check

**Overview:**
Explains how deletion/recovery behaves across modules. This section is intentionally included as a caution. In IMS, ?recovery? usually means financial recovery workflows, not a recycle-bin style undo feature for deleted records.

**Description:**
This section explains the overall data-recovery reality of the platform so users do not assume every module includes a recycle bin or simple undo flow. In IMS, the word "recovery" often refers to customer payment recovery, not restoration of deleted records. This section is included as a practical warning about how deletion and restoration typically behave across the application.

**Navigation Path:**
`Primary Sidebar > Recovery` (financial recovery only; not trash restore)

**Visual Elements:**
- Recovery menu for customer payment recovery  
- No global Trash/Recycle Bin menu visible

**Step-by-Step Usage:**
1. Use **Recovery** only for payment recovery workflows.
2. Do not treat it as deleted-record restoration.

**How the System Behaves:**
- **Prerequisites:**
Module-specific permissions.
- **Automatic Effects:**
Many deletes are permanent in tenant workflows; some modules may block delete entirely.
- **Constraints:**
Restore options are generally not exposed to tenant users.

**Data Safety Notes:**
No universal tenant restore center is present in discovered menus/routes.

**Troubleshooting:**
- If you need a deleted record restored, escalate to system admin/support; in-app self-restore is typically unavailable.

**Access Level:**
Varies by module permission.
