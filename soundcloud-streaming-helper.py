
import soundcloud

print '-------------------------------'
print '- Soundcloud streaming helper -'
print '-------------------------------\n'
client = soundcloud.Client(client_id='YOUR_CLIENT_ID')
track_url = raw_input('Insert track URL: ')
print 'Resolving url', track_url , '...'
track = client.get('/resolve', url=track_url)
print 'track id: ',  track.id
stream_url = client.get(track.stream_url, allow_redirects=False)
print 'track: ', track.title
print 'stream url: ', stream_url.location
