function calculateLoan() {
    let amount = document.getElementById("amount").value;
    let rate = document.getElementById("rate").value;
    let years = document.getElementById("years").value;

    let monthlyRate = (rate / 100) / 12;
    let numPayments = years * 12;
    let monthlyPayment = (amount * monthlyRate) / (1 - Math.pow(1 + monthlyRate, -numPayments));

    document.getElementById("result").innerText = `Monthly Payment: $${monthlyPayment.toFixed(2)}`;
}
