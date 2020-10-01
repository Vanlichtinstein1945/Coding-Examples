module.exports = {
	name: 'beep',
	description: 'boop',
	execute(message, args) {
		message.channel.send('Boop!');
	},
};