**To plan for retention during invoice**

#. Create new Vendor Bill (or Customer Invoice) in draft state.
#. In the invoice form, locate the **Payment Retention** field (below Reference).
#. Select retention type: **Percent** or **Amount**.
#. Enter the retention value (e.g., 10 for 10% or a fixed amount like 50.00).
#. System auto-calculates and displays the **Retention Amount**.
#. Post/Validate invoice as per normal.

**To make payment with retention**

#. From the posted invoice, click **Register Payment** button.
#. Payment window opens with **Suggested Retention** amount displayed.
#. Toggle **Apply Retention** to ON to apply the retention.
#. **Enforce Retention** checkbox ensures valid retention amount and account (checked by default).
#. Payment amount automatically adjusts (Total - Retention Amount).
#. Create payment as normal - Journal Entry includes retention account move line.

**Note:** While system validates retention, user can choose to ignore it by leaving Apply Retention toggle OFF.

**To return the retained amount**

#. When ready to return retained amount, create new Vendor Bill (or Customer Invoice).
#. Select the partner - **Return Retention** field shows uncleared retained amounts.
#. Select one or multiple retention payments (journal entries).
#. System auto-populates invoice lines with retained amounts.
#. Post/Validate invoice - system reconciles and clears the retention.
#. Process payment as per normal.
