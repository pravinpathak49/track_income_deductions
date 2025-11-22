document.addEventListener('DOMContentLoaded', function () {
    const ctx = document.getElementById('trendChart');

    if (ctx) {
        fetch('/api/data')
            .then(response => response.json())
            .then(data => {
                // Data comes in descending order (newest first), reverse for chart
                const entries = data.reverse();

                const labels = entries.map(e => e.date);
                const incomeData = entries.map(e => e.income);
                const deductionsData = entries.map(e => e.income - e.in_hand);
                const inHandData = entries.map(e => e.in_hand);

                new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: labels,
                        datasets: [
                            {
                                label: 'Income',
                                data: incomeData,
                                backgroundColor: 'rgba(85, 108, 214, 0.5)',
                                borderColor: 'rgba(85, 108, 214, 1)',
                                borderWidth: 1
                            },
                            {
                                label: 'Deductions',
                                data: deductionsData,
                                backgroundColor: 'rgba(224, 79, 95, 0.5)',
                                borderColor: 'rgba(224, 79, 95, 1)',
                                borderWidth: 1
                            },
                            {
                                label: 'In-Hand',
                                data: inHandData,
                                backgroundColor: 'rgba(50, 168, 82, 0.5)',
                                borderColor: 'rgba(50, 168, 82, 1)',
                                borderWidth: 1
                            }
                        ]
                    },
                    options: {
                        responsive: true,
                        scales: {
                            y: {
                                beginAtZero: true,
                                ticks: {
                                    callback: function (value) {
                                        return '$' + value.toLocaleString();
                                    }
                                }
                            }
                        },
                        plugins: {
                            tooltip: {
                                callbacks: {
                                    label: function (context) {
                                        let label = context.dataset.label || '';
                                        if (label) {
                                            label += ': ';
                                        }
                                        if (context.parsed.y !== null) {
                                            label += new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(context.parsed.y);
                                        }
                                        return label;
                                    }
                                }
                            }
                        }
                    }
                });
            })
            .catch(error => console.error('Error loading chart data:', error));
    }
});
