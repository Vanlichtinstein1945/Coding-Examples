module.exports = {
	name: 'leave',
	description: 'forces the bot to leave the voicechat',
	execute(message, args) {
		const channel = message.member.voiceChannel;
		if (!channel) return message.channel.send('Please join the bot\'s voice channel and try again.');
		channel.join()
			.then(connection => {
				channel.leave();
			});
	},
};