<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pong Game</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <canvas id="pongCanvas" width="800" height="400"></canvas>
    <script src="script.js"></script>
</body>
</html>
const paddle1 = { x: 0, y: canvas.height / 2 - paddleHeight / 2, width: paddleWidth, height: paddleHeight, dy: 5 };
const paddle2 = { x: canvas.width - paddleWidth, y: canvas.height / 2 - paddleHeight / 2, width: paddleWidth, height: paddleHeight, dy: 5 };
const ball = { x: canvas.width / 2, y: canvas.height / 2, radius: ballRadius, dx: 4, dy: 4 };

function drawPaddle(paddle) {
    context.fillStyle = '#fff';
    context.fillRect(paddle.x, paddle.y, paddle.width, paddle.height);
}

function drawBall() {
    context.beginPath();
    context.arc(ball.x, ball.y, ball.radius, 0, Math.PI * 2);
    context.fillStyle = '#fff';
    context.fill();
    context.closePath();
}

function movePaddle(paddle, up, down) {
    if (up && paddle.y > 0) {
        paddle.y -= paddle.dy;
    } else if (down && paddle.y < canvas.height - paddle.height) {
        paddle.y += paddle.dy;
    }
}

function moveBall() {
    ball.x += ball.dx;
    ball.y += ball.dy;

    if (ball.y + ball.radius > canvas.height || ball.y - ball.radius < 0) {
        ball.dy *= -1;
    }

    if (ball.x - ball.radius < 0 || ball.x + ball.radius > canvas.width) {
        ball.dx *= -1;
    }

    if (ball.x - ball.radius < paddle1.x + paddle1.width && ball.y > paddle1.y && ball.y < paddle1.y + paddle1.height) {
        ball.dx *= -1;
    }

    if (ball.x + ball.radius > paddle2.x && ball.y > paddle2.y && ball.y < paddle2.y + paddle2.height) {
        ball.dx *= -1;
    }
}

function draw() {
    context.clearRect(0, 0, canvas.width, canvas.height);
    drawPaddle(paddle1);
    drawPaddle(paddle2);
    drawBall();
    movePaddle(paddle1, upPressed, downPressed);
    movePaddle(paddle2, ball.y < paddle2.y + paddle2.height / 2, ball.y > paddle2.y + paddle2.height / 2);
    moveBall();
    requestAnimationFrame(draw);
}

document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowUp') upPressed = true;
    if (e.key === 'ArrowDown') downPressed = true;
});

document.addEventListener('keyup', (e) => {
    if (e.key === 'ArrowUp') upPressed = false;
    if (e.key === 'ArrowDown') downPressed = false;
});

draw();
