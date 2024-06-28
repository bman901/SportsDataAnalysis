var sport = GetURLParameter("sport");
var chosen_league = 0;
var chosen_season = 0;
var chosen_bet = 10;
var data = {};
var analysis = {};

window.onload = function () {
  if (sport.includes("-")) {
    capital_sport = sport.replace("-", " ");
  } else if (sport == "afl") {
    capital_sport = sport.toUpperCase();
  } else {
    capital_sport = sport;
  }
  FillInTitle(capital_sport);
  LoadImage(sport);
};

$(document).ready(function () {
  $.ajax({
    url: "",
    type: "get",
    contentType: "application/json",
    data: {
      chosen_sport: sport,
    },
    success: function (response) {
      data = response.data;

      for (let i = 0; i < data.length; i++) {
        createBtn(
          data[i]["league_name"],
          data[i]["league_id"],
          "league_btns",
          "btn-primary"
        );
      }

      GetChosenLeague(data);
    },
  });
});

function GetURLParameter(sParam) {
  let sPageURL = window.location.search.substring(1);
  let sURLVariables = sPageURL.split("&");
  for (let i = 0; i < sURLVariables.length; i++) {
    let sParameterName = sURLVariables[i].split("=");
    if (sParameterName[0] == sParam) {
      return sParameterName[1];
    }
  }
}

function createBtn(btn_name, btn_id, location, class_name) {
  let btn = document.createElement("button");
  btn.className = "btn " + class_name;
  btn.id = btn_id;
  btn.textContent = btn_name;
  let body = document.getElementById(location);
  body.appendChild(btn);
}

function TitleCase(str) {
  let splitStr = str.split(" ");
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

function LoadImage(sport) {
  document.getElementById("sport_img").src = `../static/img/${sport}.jpg`;
}

function GetChosenLeague(data) {
  const league_btn = document.querySelectorAll(".btn-primary");

  for (let i = 0; i < league_btn.length; i++) {
    league_btn[i].addEventListener("click", function () {
      chosen_league = league_btn[i].id;
      LoadAvailableSeasons(data, chosen_league);
      document.getElementById("season_text").innerHTML =
        "Choose season to review:";
      document.getElementById("perc_fav").innerHTML =
        "Please choose a season to review";
    });
  }
}

// Add an All Seasons button?

function LoadAvailableSeasons(data, chosen_league) {
  document.getElementById("season_btns").innerHTML = "";
  for (let i = 0; i < data.length; i++) {
    if (data[i]["league_id"] == chosen_league) {
      for (let j = 0; j < data[i]["seasons"].length; j++) {
        createBtn(
          data[i]["seasons"][j],
          data[i]["seasons"][j],
          "season_btns",
          "btn-secondary"
        );
      }
    }
  }

  GetChosenSeason();
}

function GetChosenSeason() {
  const season_btn = document.querySelectorAll(".btn-secondary");

  for (let i = 0; i < season_btn.length; i++) {
    season_btn[i].addEventListener("click", function () {
      chosen_season = season_btn[i].id;
      GetAnalysisData();
    });
  }
}

function CreateInputs() {
  $.ajax({
    url: "",
    type: "get",
    contentType: "application/json",
    data: {
      chosen_sport: sport,
      chosen_league: chosen_league,
      chosen_season: chosen_season,
      chosen_bet: chosen_bet,
    },
    success: function (response) {
      analysis = response.analysis;
      PercentageAnalysis(analysis);
      PlotGraph();
      CreateBetInput();
      Report_Betting(analysis);
    },
  });
}

function GetAnalysisData() {
  $.ajax({
    url: "",
    type: "get",
    contentType: "application/json",
    data: {
      chosen_sport: sport,
      chosen_league: chosen_league,
      chosen_season: chosen_season,
      chosen_bet: chosen_bet,
    },
    success: function (response) {
      analysis = response.analysis;
      PercentageAnalysis(analysis);
      PlotGraph();
      CreateBetInput();
      Report_Betting(analysis);
    },
  });
}

function PercentageAnalysis(analysis) {
  if (analysis["perc_fav"]) {
    document.getElementById("perc_fav").innerHTML = analysis["perc_fav"];
  } else {
    document.getElementById("perc_fav").innerHTML =
      "No data for the chosen season";
  }
}

function Report_Betting(analysis) {
  if (analysis["bet_on_fav"]) {
    document.getElementById("betting_output").innerHTML =
      analysis["bet_on_fav"];
  } else {
    document.getElementById("betting_output").innerHTML = "";
  }
}

function GetChosenBet() {
  let bet_input_val = document.getElementById("bet");
  bet_input_val.addEventListener("input", function () {
    chosen_bet = bet_input_val.value;
    console.log(chosen_bet);
    if (chosen_bet == "") {
      document.getElementById("betting_output").innerHTML =
        "Please enter a bet";
    } else if (chosen_bet < 0) {
      document.getElementById("betting_output").innerHTML =
        "Please enter a positive number";
    } else {
      GetAnalysisData();
    }
  });
}

function PlotGraph() {
  document.getElementById("sport_img").src = "../static/img/fav_plot.png";
}

function CreateBetInput() {
  if (document.getElementById("betting_input").innerHTML == "") {
    let bet_input = document.createElement("input");
    bet_input.type = "number";
    bet_input.min = "0";
    bet_input.id = "bet";
    bet_input.inputmode = "decimal";
    bet_input.pattern = "(^£$)|(^£d{1,3}(,d{3})*?$)"; // ^\\$?(([1-9](\\d*|\\d{0,2}(,\\d{3})*))|0)(\\.\\d{1,2})?$
    bet_input.required = "";
    bet_input.value = "10";
    bet_input.class = "";
    let body = document.getElementById("betting_input");
    body.appendChild(bet_input);
  }
}
