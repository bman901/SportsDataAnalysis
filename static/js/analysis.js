var sport = GetURLParameter("sport");

window.onload = function () {
  if (sport == "all-sports") {
    capital_sport = sport.replace("-", " ");
  } else if (sport == "afl") {
    capital_sport = sport.toUpperCase();
  } else {
    capital_sport = sport;
  }
  FillInTitle(capital_sport);
  FillInVar(sport);
};

$(document).ready(function () {
  $(".btn").click(function () {
    $.ajax({
      url: "",
      type: "get",
      contentType: "application/json",
      data: {
        chosen_sport: sport,
      },
      success: function (response) {
        document.getElementById("percentage_fav").innerHTML =
          data[0]["perc_fav"];
      },
    });
  });
});

$(document).ready(function () {
  $.ajax({
    url: "",
    type: "get",
    contentType: "application/json",
    data: {
      chosen_sport: sport,
    },
    success: function (response) {
      var data = response.data;

      for (let i = 0; i < data.length; i++) {
        createBtn(data[i]["league_name"]);
      }
    },
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

function createBtn(btn_name) {
  var btn = document.createElement("button");
  btn.className = "btn btn-primary";
  btn.textContent = btn_name;
  document.body.appendChild(btn);
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

function FillInTitle(sport) {
  document.getElementById("title").innerHTML = document
    .getElementById("title")
    .innerHTML.replace("?sport?", TitleCase(sport));
}

function FillInVar(sport) {
  document.getElementById("league_btns").innerHTML = document
    .getElementById("league_btns")
    .innerHTML.replace("var_sport", sport);
}
