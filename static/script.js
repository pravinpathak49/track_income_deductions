document.addEventListener('DOMContentLoaded', function () {
    const addDeductionBtn = document.getElementById('add-deduction-btn');
    const deductionsContainer = document.getElementById('deductions-container');
    const incomeInput = document.getElementById('income');
    const inHandInput = document.getElementById('in_hand');
    const calcPreview = document.getElementById('calc-preview');

    // Add new deduction row
    if (addDeductionBtn) {
        addDeductionBtn.addEventListener('click', function () {
            const row = document.createElement('div');
            row.className = 'deduction-row';
            row.innerHTML = `
                <input type="text" name="deduction_name[]" placeholder="Deduction Name" required>
                <input type="number" name="deduction_amount[]" placeholder="Amount" step="0.01" class="deduction-amount" required>
                <button type="button" class="btn-danger remove-row" style="padding: 0 10px;">&times;</button>
            `;
            deductionsContainer.appendChild(row);

            // Add event listener to new remove button
            row.querySelector('.remove-row').addEventListener('click', function () {
                row.remove();
                calculateInHand();
            });

            // Add event listener to new input for calculation
            row.querySelector('.deduction-amount').addEventListener('input', calculateInHand);
        });
    }

    // Calculate in-hand preview
    function calculateInHand() {
        const income = parseFloat(incomeInput.value) || 0;
        let totalDeductions = 0;

        document.querySelectorAll('.deduction-amount').forEach(input => {
            totalDeductions += parseFloat(input.value) || 0;
        });

        const calculatedInHand = income - totalDeductions;
        calcPreview.textContent = '$' + calculatedInHand.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });

        // Optional: Auto-fill the in-hand input if user hasn't manually edited it? 
        // For now, let's just show the preview so the user can verify.
        // Or we can just set it:
        inHandInput.value = calculatedInHand.toFixed(2);
    }

    if (incomeInput) {
        incomeInput.addEventListener('input', calculateInHand);
        // Initial listener for the first deduction row
        document.querySelectorAll('.deduction-amount').forEach(input => {
            input.addEventListener('input', calculateInHand);
        });
    }

    // Delete confirmation handler
    const deleteModal = document.getElementById('deleteModal');
    const cancelDeleteBtn = document.getElementById('cancelDelete');
    const confirmDeleteBtn = document.getElementById('confirmDelete');
    let formToDelete = null;

    document.addEventListener('click', function (e) {
        if (e.target && e.target.classList.contains('btn-delete-confirm')) {
            e.preventDefault();
            e.stopPropagation();
            const entryId = e.target.getAttribute('data-entry-id');
            formToDelete = document.getElementById('delete-form-' + entryId);
            if (deleteModal) {
                deleteModal.style.display = 'flex';
                // Small timeout to allow display:flex to apply before adding show class for transition
                setTimeout(() => {
                    deleteModal.classList.add('show');
                }, 10);
            }
        }
    });

    if (cancelDeleteBtn) {
        cancelDeleteBtn.addEventListener('click', function () {
            if (deleteModal) {
                deleteModal.classList.remove('show');
                setTimeout(() => {
                    deleteModal.style.display = 'none';
                }, 300); // Match transition duration
            }
            formToDelete = null;
        });
    }

    if (confirmDeleteBtn) {
        confirmDeleteBtn.addEventListener('click', function () {
            if (formToDelete) {
                formToDelete.submit();
            }
        });
    }

    // Close modal if clicking outside content
    if (deleteModal) {
        deleteModal.addEventListener('click', function (e) {
            if (e.target === deleteModal) {
                deleteModal.classList.remove('show');
                setTimeout(() => {
                    deleteModal.style.display = 'none';
                }, 300);
            }
        });
    }
});
