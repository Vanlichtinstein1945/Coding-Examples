const { Attachment } = require('discord.js');
const fs = require('fs');

module.exports = {
	name: 'quote',
	description: 'quote things',
	execute(message, args) {
		const randomQuotes = fs.readFileSync('quotes.txt').toString();
		const quotes = randomQuotes.split("\n");
		const quote = quotes[Math.floor(Math.random() * Math.floor(quotes.length))];
		const quote_changed = quote.replace(/[\r\n]+/gm, "");
		
		message.channel.send(`\'${quote_changed}\' - Quote ?`, {
			files: [
				'./images/quote.png'
			]
		});
	},
};