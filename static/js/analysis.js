var sport = GetURLParameter("sport");

window.onload = function () {
  if (sport == "all-sports") {
    capital_sport = sport.replace("-", " ");
  } else if (sport == "afl") {
    capital_sport = sport.toUpperCase();
  }
  FillInSport(capital_sport);
};

$(document).ready(function () {
  $(".btn").click(function () {
    $.ajax({
      url: "",
      type: "get",
      contentType: "application/json",
      data: {
        btn_sport: sport,
      },
    });
  });
});

function GetURLParameter(sParam) {
  var sPageURL = window.location.search.substring(1);
  var sURLVariables = sPageURL.split("&");
  for (var i = 0; i < sURLVariables.length; i++) {
    var sParameterName = sURLVariables[i].split("=");
    if (sParameterName[0] == sParam) {
      return sParameterName[1];
    }
  }
}

function TitleCase(str) {
  var splitStr = str.split(" ");
  for (var i = 0; i < splitStr.length; i++) {
    // Assign it back to the array
    splitStr[i] =
      splitStr[i].charAt(0).toUpperCase() + splitStr[i].substring(1);
  }
  // Directly return the joined string
  return splitStr.join(" ");
}

function FillInSport(sport) {
  document.getElementById("title").innerHTML = document
    .getElementById("title")
    .innerHTML.replace("?sport?", TitleCase(sport));
}
