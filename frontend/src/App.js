fetch("http://localhost:5000/")
.then(r => r.json())
.then(data => {
document.body.innerHTML = `<h1>Frontend працює!</h1><p>Backend каже: ${data.message}</p>`;
});
