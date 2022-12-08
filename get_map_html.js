document.getElementById("selectedDate")
.addEventListener("change", function() {
    var input = this.value;
    fetchHtml(input);
});

function fetchHtml(date) {
    const url = 'https://qx82d7.deta.dev/wifi/map?date=' + date;
    fetch(url).then((response) => {
        return response.text();
    }).then((html_string) => {
        document.getElementById('map_frame').srcdoc = html_string;
    });
};
