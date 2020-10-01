module.exports = {
	name: 'play',
	description: 'plays songs from youtube',
	execute(message, args) {
		const channel = message.member.voiceChannel;
		if (!channel) return message.channel.send('Please join a voice channel and try again.');
		channel.join()
			.then(connection => {
				console.log('Connected!');
				const dispatcher = connection.playFile('./music/test.mp3');
				dispatcher.setVolume(.05);
				
				dispatcher.on('end', end => {
					console.log('Song finished and disconnecting!');
					channel.leave();
				})
			})
			.catch(console.error);
	},
};