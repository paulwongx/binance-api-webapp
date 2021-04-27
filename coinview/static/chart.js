const chart = LightweightCharts.createChart(document.getElementById("chart"), {
	width: 600,
	height: 300,
	layout: {
		backgroundColor: "#000000",
		textColor: "rgba(255, 255, 255, 0.9)",
	},
	grid: {
		vertLines: {
			color: "rgba(197, 203, 206, 0.5)",
		},
		horzLines: {
			color: "rgba(197, 203, 206, 0.5)",
		},
	},
	crosshair: {
		mode: LightweightCharts.CrosshairMode.Normal,
	},
	rightPriceScale: {
		borderColor: "rgba(197, 203, 206, 0.8)",
	},
	timeScale: {
		borderColor: "rgba(197, 203, 206, 0.8)",
	},
});

const candleSeries = chart.addCandlestickSeries({
	upColor: "rgba(0, 144, 0, 1)",
	downColor: "rgba(255, 0, 0, 1)",
	borderDownColor: "rgba(255, 0, 0, 1)",
	borderUpColor: "rgba(0, 144, 0, 1)",
	wickDownColor: "rgba(255, 0, 0, 1)",
	wickUpColor: "rgba(0, 144, 0, 1)",
});

fetch("http://localhost:5000/history")
	.then(r => r.json())
	.then(res => {
		// console.log(res);
		candleSeries.setData(res);
	})
	.catch(err => console.log(err));

let binanceSocket = new WebSocket(
	"wss://stream.binance.com:9443/ws/ethusdt@kline_1d"
);

binanceSocket.onmessage = event => {
	// console.log(event.data);

	let message = JSON.parse(event.data);

	let candlestick = message.k;
	// console.log(candlestick);

	candleSeries.update({
		time: candlestick.t / 1000,
		open: candlestick.o,
		high: candlestick.h,
		low: candlestick.l,
		close: candlestick.c,
	});
};
