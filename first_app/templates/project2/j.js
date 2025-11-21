var player1 = prompt("Player One: Enter your name, you will be Blue");
var player1Color = 'rgb(86, 151, 255)';

var player2 = prompt("Player Two: Enter your name, you will be Red");
var player2Color = 'rgb(237, 45, 73)';

var game_on = true;
var table = $('table.board tr');

var currentPlayer = 1;
var currentName = player1;
var currentColor = player1Color;

$('h3').text(currentName + ": it is your turn, pick a column to drop your chip!");

function reportWin(rowNum, colNum) {
  console.log("You won starting at this row, col");
  console.log(rowNum);
  console.log(colNum);
}

// Simplified color check
function returnColor(row, col) {
  return table.eq(row).find('td').eq(col).find('button').css('background-color');
}

// Mark a player on button (new fix)
function markPlayer(row, col, player) {
  table.eq(row).find('td').eq(col).find('button').attr('data-player', player);
}

function returnPlayer(row, col) {
  return table.eq(row).find('td').eq(col).find('button').attr('data-player');
}

// Drop logic
function checkBottom(col) {
  for (var row = 5; row > -1; row--) {
    var colorReport = returnColor(row, col);
    if (colorReport === 'rgb(128, 128, 128)') {
      return row;
    }
  }
}

function colorMatchCheck(p1, p2, p3, p4) {
  return (p1 && p1 === p2 && p1 === p3 && p1 === p4);
}

// WIN CHECKS
function horizontalWinCheck() {
  for (var row = 0; row < 6; row++) {
    for (var col = 0; col < 4; col++) {
      var p1 = returnPlayer(row, col);
      var p2 = returnPlayer(row, col + 1);
      var p3 = returnPlayer(row, col + 2);
      var p4 = returnPlayer(row, col + 3);
      if (colorMatchCheck(p1, p2, p3, p4)) {
        reportWin(row, col);
        return true;
      }
    }
  }
}

function verticalWinCheck() {
  for (var col = 0; col < 7; col++) {
    for (var row = 0; row < 3; row++) {
      var p1 = returnPlayer(row, col);
      var p2 = returnPlayer(row + 1, col);
      var p3 = returnPlayer(row + 2, col);
      var p4 = returnPlayer(row + 3, col);
      if (colorMatchCheck(p1, p2, p3, p4)) {
        reportWin(row, col);
        return true;
      }
    }
  }
}

function diagonalWinCheck() {
  for (var col = 0; col < 4; col++) {
    for (var row = 0; row < 3; row++) {
      var p1 = returnPlayer(row, col);
      var p2 = returnPlayer(row + 1, col + 1);
      var p3 = returnPlayer(row + 2, col + 2);
      var p4 = returnPlayer(row + 3, col + 3);
      if (colorMatchCheck(p1, p2, p3, p4)) {
        reportWin(row, col);
        return true;
      }
    }
  }

  for (var col = 0; col < 4; col++) {
    for (var row = 5; row > 2; row--) {
      var p1 = returnPlayer(row, col);
      var p2 = returnPlayer(row - 1, col + 1);
      var p3 = returnPlayer(row - 2, col + 2);
      var p4 = returnPlayer(row - 3, col + 3);
      if (colorMatchCheck(p1, p2, p3, p4)) {
        reportWin(row, col);
        return true;
      }
    }
  }
}

function gameEnd(winnerName) {
  $('h3').fadeOut('fast');
  $('h2').fadeOut('fast');
  $('h1').text(winnerName + " has won the game! please refresh the page to play again").css("color", "white");
}

$('.board button').on('click', function () {
  var col = $(this).closest('td').index();
  var bottomAvail = checkBottom(col);

  var color = returnColor(bottomAvail, col);

  if (color === 'rgb(128, 128, 128)') {
    table.eq(bottomAvail).find('td').eq(col).find('button')
      .css('background-color', currentColor)
      .attr('data-player', currentPlayer);

    if (horizontalWinCheck() || verticalWinCheck() || diagonalWinCheck()) {
      gameEnd(currentName);
      return;
    }

    // Switch player
    currentPlayer = currentPlayer === 1 ? 2 : 1;
    currentName = currentPlayer === 1 ? player1 : player2;
    currentColor = currentPlayer === 1 ? player1Color : player2Color;

    $('h3').text(currentName + ": it's your turn, pick a column to drop your chip!");
  }
});
