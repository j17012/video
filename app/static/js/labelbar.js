// jQueryプラグイン「LabelBar.js」
// Version: 20210219.1
//
// 引数
// (Object){
//   labels: (Array)[(String)labelName, ...],                ラベル名
//   barColor: (Object){labelName: (colorCode), ...},        ラベルバーカラー
//   data: (Array)[(Array)[sec, label1, label2, ...], ...],  データ（先頭行に見出しを含まない）
//   options: (Object){	                                     オプション
//     canvasPadding: 5,                                       Canvas内側の余白
//     spacing: 10,                                            隙間
//     fontSize: 20,                                           フォントサイズ
//     labelWidth: 100,                                        ラベル名の表示幅
//     graphBoder: true,                                       グラフ枠の有無
//     graphBoderColor: "#888",                                グラフ枠の色
//     graphRuledLineRow: true,                                グラフ罫線の有無
//     graphRuledLineRowColor: "#888"                          グラフ罫線の色
//   }
// }

$(function() {
	var methods = {
		init: function(config) {
			// *
			// 引数
			// *
			var labels = config.labels;
			var barColor = config.barColor;
			var data = config.data;
			var options = $.extend(true, {
				canvasPadding: 5,
				spacing: 10,
				fontSize: 20,
				labelWidth: 100,
				graphBoder: true,
				graphBoderColor: "#888",
				graphRuledLineRow: true,
				graphRuledLineRowColor: "#888"
			}, config.options);

			// *
			// データテーブル
			// *
			var table = "<table id=\"label-data\" border=\"1\" style=\"max-width:100%; border-collapse:collapse;\">";
			table += "<tr><th></th>";
			$(labels).each(function(i, item) {
				table += "<th>" + item + "</th>";
			});
			table += "</tr>";
			$(data).each(function(i, row) {
				table += "<tr>";
				$(row).each(function(j) {
					table += "<td>" + row[j] + "</td>";
				});
				table += "</tr>";
			});
			table += "</table>";

			$("#label-data").remove();
			this.after(table);

			// *
			// ラベルバー
			// *
			this.css({"display": "block", "width": "100%"});

			var canvas = this[0];
			var ctx = canvas.getContext("2d");
			// サイズ定義
			options.canvasPadding *= devicePixelRatio;
			options.spacing *= devicePixelRatio;
			options.fontSize *= devicePixelRatio;
			options.labelWidth *= devicePixelRatio;
			var lineHeight = options.fontSize + options.spacing;
			// Canvasサイズ
			canvas.width = this.width() * devicePixelRatio;
			canvas.height = (options.canvasPadding *2 + (lineHeight * (labels.length +1)));
			// 塗、フォントサイズ
			ctx.fillStyle = "#000";
			ctx.font = options.fontSize + "px sans";
			// グラフ範囲
			var graph = {
				x: options.canvasPadding + options.labelWidth + options.spacing,
				y: options.canvasPadding + lineHeight,
				w: canvas.width - options.canvasPadding *2 - options.labelWidth - options.spacing,
				h: lineHeight * (labels.length),
			};
			// 最初と最後の時間
			var secY = options.canvasPadding + options.fontSize;
			ctx.fillText(data[0][0], graph.x, secY);
			ctx.textAlign = "end";
			ctx.fillText(data[data.length-1][0], graph.x + graph.w, secY);
			ctx.textAlign = "start";
			// ラベル
			$(labels).each(function(i, item) {
				ctx.fillStyle = barColor[item];
				ctx.fillRect(options.canvasPadding, graph.y + options.spacing /2 + (lineHeight * i), options.fontSize /2, options.fontSize)
				ctx.fillStyle = "#000";
				ctx.fillText(item, options.canvasPadding + options.fontSize, graph.y + options.spacing /2 + (options.fontSize * (i +1)) + (options.spacing * i), options.labelWidth - options.fontSize);
			});
			// バー
			$(data).each(function(i, row) {
				$(row).each(function(j, value) {
					if (j == 0) return;
					if (value == 0) return;
					var labelNum = j -1;
					var barWidth = graph.w / data.length;
					ctx.fillStyle = barColor[labels[labelNum]];
					ctx.fillRect(graph.x + barWidth * i, graph.y + options.spacing /2 + (lineHeight * labelNum), barWidth, options.fontSize);
				});
			});
			// グラフ線
			if (options.graphBoder) {
				if (options.graphRuledLineRow) {
					$(labels).each(function(i) {
						ctx.fillStyle = options.graphRuledLineRowColor;
						ctx.fillRect(graph.x, graph.y + (lineHeight * (i +1)) -1, graph.w, 1);
					});
				}
				ctx.strokeStyle = options.graphBoderColor;
				ctx.strokeRect(graph.x, graph.y, graph.w, graph.h);
			}
		}
	};

	$.fn.labelBar = function(method) {
		if (methods[method]) {
			return methods[method].apply(this, Array.prototype.slice.call(arguments, 1));
		} else if (typeof method === 'object' || ! method) {
			return methods.init.apply(this, arguments);
		} else {
			$.error('Method ' +  method + ' does not exist on jQuery.labelBar');
		}
	};
});
