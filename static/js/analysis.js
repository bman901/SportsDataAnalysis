var sport = GetURLParameter("sport");
var chosen_league = 0;
var chosen_season = 0;

window.onload = function () {
  if (sport == "all-sports") {
    capital_sport = sport.replace("-", " ");
  } else if (sport == "afl") {
    capital_sport = sport.toUpperCase();
  } else {
    capital_sport = sport;
  }
  FillInTitle(capital_sport);
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
  // document.body.appendChild(btn);
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

function GetChosenLeague(data) {
  const league_btn = document.querySelectorAll(".btn-primary");

  for (let i = 0; i < league_btn.length; i++) {
    league_btn[i].addEventListener("click", function () {
      chosen_league = league_btn[i].id;
      LoadAvailableSeasons(data, chosen_league);
    });
  }
}

// Currently only loading current season
function LoadAvailableSeasons(data, chosen_league) {
  document.getElementById("season_btns").innerHTML = "";
  for (let i = 0; i < data.length; i++) {
    if (data[i]["league_id"] == chosen_league) {
      createBtn(
        data[i]["current_season"],
        data[i]["current_season"],
        "season_btns",
        "btn-secondary"
      );
    }
  }

  GetChosenSeason();
}

function GetChosenSeason() {
  const season_btn = document.querySelectorAll(".btn-secondary");

  for (let i = 0; i < season_btn.length; i++) {
    season_btn[i].addEventListener("click", function () {
      chosen_season = season_btn[i].id;
      console.log(chosen_league, chosen_season);
    });
  }
}
