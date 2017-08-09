import sqlite3
from passlib.apps import custom_app_context as pwd_context

conn = sqlite3.connect("website.db") # or use :memory: to put it in RAM cursor = conn.cursor()
cursor= conn.cursor()

cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre, img_url) VALUES('5', 'organized crime', '19.00', 'The Godfather', '238', 'drama', 'https://image.tmdb.org/t/p/w500/rPdtLWNsZmAtoZl9PK7S2wE3qiS.jpg')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre, img_url) VALUES('4', 'prison escape', '20.00', 'The Shawshank Redemption', '278', 'drama', 'https://image.tmdb.org/t/p/w500/9O7gLzmreU0nGkIB6K3BsJbzvNv.jpg')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre, img_url) VALUES('3', 'upstander in Nazi germany during Holocaust', '21.00', 'Schindler\'s List', '424', 'drama', 'https://image.tmdb.org/t/p/w500/yPisjyLweCl1tbgwgtzBCNCBle.jpg')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre, img_url) VALUES('2', 'boxer journey', '22.00', 'Raging Bull', '1578', 'drama', 'https://image.tmdb.org/t/p/w500/cbTfaMrWpZWwF3mY40v1SKaAVCx.jpg')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre, img_url) VALUES('6', 'expatriate encounters a former lover', '23.00', 'Casablanca', '289', 'romance', 'https://image.tmdb.org/t/p/w500/wOBKAoUJZb5qTsWv5XXvVV2vUzz.jpg')")

cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre, img_url) VALUES('5', 'Three office workers strike back at their evil employers by hatching a hapless attempt to embezzle money', '19.00', 'Office Space', '1542', 'comedy', 'https://image.tmdb.org/t/p/w500/iO9aZzrfmMvm3IqkFiQyuuUMLh2.jpg')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre, img_url) VALUES('4', 'Three American brothers who have not spoken to each other in a year set off on a train voyage across India with a plan to find themselves and bond with each other', '20.00', 'The Darjeeling Limited', '4538', 'comedic drama', 'https://image.tmdb.org/t/p/w500/47AGp0EKNMjqBBPaxRYDW0Sc5If.jpg')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre, img_url) VALUES('3', 'a teenager who was arrested by the US Secret Service and banned from using a computer for writing a computer virus discovers a plot by a nefarious hacker', '21.00', 'Hackers', '10428', 'adventure', 'https://image.tmdb.org/t/p/w500/uu62T87qkLkapeuu7ArlnQ6tAap.jpg')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre, img_url) VALUES('2', 'an adventurous young clownfish, is unexpectedly taken from his Great Barrier Reef home', '22.00', 'Finding Nemo', '12', 'animated drama', 'https://image.tmdb.org/t/p/w500/syPWyeeqzTQIxjIUaIFI7d0TyEY.jpg')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre, img_url) VALUES('6', 'An apocalyptic story set in the furthest reaches of our planet', '23.00', 'Mad Max: Fury Road', '76341', 'adventure', 'https://image.tmdb.org/t/p/w500/kqjL17yufvn9OVLyXYpvtyrFfak.jpg')")

cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre, img_url) VALUES('5', 'After a gentle alien becomes stranded on Earth, the being is discovered and befriended by a young boy named Elliott', '19.00', 'E.T. the Extra-Terrestrial', '601', 'sci-fi drama', 'https://image.tmdb.org/t/p/w500/8htLKK03TJjKZOXJgihZCu8v0P.jpg')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre, img_url) VALUES('4', 'Vampire housemates try to cope with the complexities of modern life and show a newly turned hipster some of the perks of being undead', '20.00', 'What We Do in the Shadows', '246741', 'comedy', 'https://image.tmdb.org/t/p/w500/pDKJFVofjfQj0cUa7z4NAXZavW.jpg')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre, img_url) VALUES('3', 'Determined to prove herself, Officer Judy Hopps, the first bunny on Zootopias police force, jumps at the chance to crack her first case', '21.00', 'Zootopia', '269149', 'animated comedy', 'https://image.tmdb.org/t/p/w500/sM33SANp9z6rXW8Itn7NnG1GOEs.jpg')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre, img_url) VALUES('2', 'a wrestler long past his prime cant resist the lure of the ring and readies himself for a comeback', '22.00', 'The Wrestler', '12163', 'drama', 'https://image.tmdb.org/t/p/w500/huooRmB7yksJyVVSkqOgitxlCec.jpg')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre, img_url) VALUES('6', 'The Fantastic Mr Fox bored with his current life, plans a heist against the three local farmers', '23.00', 'Fantastic Mr Fox', '10315', 'animation', 'https://image.tmdb.org/t/p/w500/750pfEttsYAVmynRg2vmt1AXh4q.jpg')")

cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre, img_url) VALUES('5', 'An estranged family of former child prodigies reunites when their father announces he has a terminal illness', '19.00', 'The Royal Tenenbaums', '9428', 'comedic drama', 'https://image.tmdb.org/t/p/w500/sNlz540u565f0fGK6CB0379cIJE.jpg')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre, img_url) VALUES('4', 'When a beautiful first-grade teacher arrives at a prep school, she soon attracts the attention of an ambitious teenager named Max', '20.00', 'Rushmore', '11545', 'quirky drama', 'https://image.tmdb.org/t/p/w500/q3ov1BFTCRWoR9Q6udaRbmgfWwg.jpg')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre, img_url) VALUES('3', 'Upon his release from a mental hospital following a nervous breakdown, the directionless Anthony joins his friend Dignan, who seems far less sane than the former', '21.00', 'Bottle Rocket', '13685', 'drama', 'https://image.tmdb.org/t/p/w500/iuO10cRKrMfql5yc8YTgdfHt7gR.jpg')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre, img_url) VALUES('2', 'The discovery of a severed human ear found in a field leads a young man on an investigation related to a beautiful, mysterious nightclub singer and a group of criminals who have kidnapped her child', '22.00', 'Blue Velvet', '793', 'drama', 'https://image.tmdb.org/t/p/w500/psJb2NQKUWDQyhMRV3hoEWk60gS.jpg')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre, img_url) VALUES('6', 'When the renegade crew of Serenity agrees to hide a fugitive on their ship, they find themselves in an action-packed battle with the relentless military might of a totalitarian regime', '23.00', 'Serenity', '16320', 'space opera', 'https://image.tmdb.org/t/p/w500/1Hq659V31ER9pQQvVBUUJbwR7NT.jpg')")

cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre, img_url) VALUES('5', 'Five college friends spend the weekend at a remote cabin in the woods, where they get more than they bargained for', '19.00', 'The Cabin in the Woods', '22970', 'thriller', 'https://image.tmdb.org/t/p/w500/utfJuX6DfR28Mv2FMfnPFAYOmTU.jpg')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre, img_url) VALUES('4', 'friends witness a horrifying train derailment and are lucky to escape with their lives. They soon discover that the catastrophe was no accident, as a series of unexplained events and disappearances soon follows', '20.00', 'Super 8', '37686', 'suspense', 'https://image.tmdb.org/t/p/w500/1JAKnHjENVz1adurNjtsWZnVQGY.jpg')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre, img_url) VALUES('3', 'Five young New Yorkers throw their friend a going-away party the night that a monster the size of a skyscraper descends upon the city', '21.00', 'Cloverfield', '7191', 'action sci-fi', 'https://image.tmdb.org/t/p/w500/as01o40tJ2FhtheqeXf7bVZ0EQO.jpg')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre, img_url) VALUES('2', 'After a car accident, Michelle awakens to find herself in a mysterious bunker with two men named Howard and Emmett', '22.00', '10 Cloverfield Lane', '7191', 'suspense', 'https://image.tmdb.org/t/p/w500/aeiVxTSTeGJ2ICf1iSDXkF3ivZp.jpg')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre, img_url) VALUES('6', 'Walt Kowalski is a widower who holds onto his prejudices despite the changes in his Michigan neighborhood and the world around him', '23.00', 'Gran Torino', '2', 'drama', 'https://image.tmdb.org/t/p/w500/yeBc5vpEiqIAZrbVQnl833GlBEi.jpg')")

cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre, img_url) VALUES('5', 'A Hollywood stunt performer who moonlights as a wheelman for criminals discovers that a contract has been put on him after a heist gone wrong', '19.00', 'Drive', '64690', 'action crime', 'https://image.tmdb.org/t/p/w500/nu7XIa67cXc2t7frXCE5voXUJcN.jpg')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre, img_url) VALUES('4', 'A fading actor best known for his portrayal of a popular superhero attempts to mount a comeback by appearing in a Broadway play', '20.00', 'Birdman', '194662', 'quirky drama', 'https://image.tmdb.org/t/p/w500/rSZs93P0LLxqlVEbI001UKoeCQC.jpg')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre, img_url) VALUES('3', 'Cobb, a skilled thief who commits corporate espionage by infiltrating the subconscious of his targets is offered a chance to regain his old life', '21.00', 'Inception', '27205', 'psychological thriller', 'https://image.tmdb.org/t/p/w500/qmDpIHrmpJINaRKAfWQfftjCdyi.jpg')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre, img_url) VALUES('2', 'When Lou Bloom, desperate for work, muscles into the world of L.A. crime journalism, he blurs the line between observer and participant to become the star of his own story', '22.00', 'Nightcrawler', '242582', 'thriller', 'https://image.tmdb.org/t/p/w500/8oPY6ULFOTbAEskySNhgsUIN4fW.jpg')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre, img_url) VALUES('6', 'Annies life is a mess. But when she finds out her lifetime best friend is engaged, she must serve as Lillian’s maid of honor', '23.00', 'Bridesmaids', '55721', 'comedy', 'https://image.tmdb.org/t/p/w500/x5ucaJZ4FP589Gn3I8l3ZFV3Nl8.jpg')")
conn.commit();

#Delete all rows in tables
cursor.execute("DELETE FROM users");
cursor.execute("DELETE FROM inventory");
cursor.execute("DELETE FROM mediaType");
cursor.execute("DELETE FROM orders");
cursor.execute("DELETE FROM payment");

#insert test cases
media = ["DVD", "BluRay", "VHS"]
cursor.execute("INSERT INTO mediaType(media) VALUES('DVD')");
cursor.execute("INSERT INTO mediaType(media) VALUES('BluRay')");
cursor.execute("INSERT INTO mediaType(media) VALUES('VHS')");

#Changed to make sure passwords are hashed for each user
cursor.execute("INSERT INTO users(username, password, email) VALUES('a', ?, 'a@aol.com')", (pwd_context.hash("a"),))
cursor.execute("INSERT INTO users(username, password, email) VALUES('b', ?, 'b@aol.com')", (pwd_context.hash("b"),))
cursor.execute("INSERT INTO users(username, password, email) VALUES('c', ?, 'c@aol.com')", (pwd_context.hash("c"),))
cursor.execute("INSERT INTO users(username, password, email) VALUES('d', ?, 'd@aol.com')", (pwd_context.hash("d"),)) 
cursor.execute("INSERT INTO users(username, password, email) VALUES('e', ?, 'e@aol.com')", (pwd_context.hash("e"),))
#conn.commit();

cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre) VALUES('5', 'organized crime', '19.00', 'The Godfather', '1', 'drama')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre) VALUES('4', 'prison escape', '20.00', 'The Shawshank Redemption', '2', 'drama')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre) VALUES('3', 'upstander in Nazi germany during Holocaust', '21.00', 'Schindlers List', '1', 'drama')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre) VALUES('2', 'boxer journey', '22.00', 'Raging Bull', '1', 'drama')")
cursor.execute("INSERT INTO inventory(quantity, description, price, name, mediaID, genre) VALUES('6', 'expatriate encounters a former lover', '23.00', 'Casablanca', '2', 'romance')")
#conn.commit();

cursor.execute("INSERT INTO payment(ccName, address, ccNumber, exp, ccv, userID) VALUES('a', '123 Test Street', '1234123412341234', '00/0000', '123', '1')")
cursor.execute("INSERT INTO payment(ccName, address, ccNumber, exp, ccv, userID) VALUES('b', '124 Test Street', '1234123412341235', '00/0001', '124', '2')")
cursor.execute("INSERT INTO payment(ccName, address, ccNumber, exp, ccv, userID) VALUES('c', '125 Test Street', '1234123412341236', '00/0002', '125', '3')")
cursor.execute("INSERT INTO payment(ccName, address, ccNumber, exp, ccv, userID) VALUES('d', '126 Test Street', '1234123412341237', '00/0003', '126', '4')")
cursor.execute("INSERT INTO payment(ccName, address, ccNumber, exp, ccv, userID) VALUES('e', '127 Test Street', '1234123412341238', '00/0004', '127', '5')")
#conn.commit();

cursor.execute("INSERT INTO orders(total, quantity, userID, itemID, ccID) VALUES('23.45', '1', (SELECT userID FROM users WHERE username='a'), (SELECT itemID FROM inventory WHERE name = 'Raging Bull'), '12345')")
cursor.execute("INSERT INTO orders(total, quantity, userID, itemID, ccID) VALUES('543.67', '2', (SELECT userID FROM users WHERE username = 'b'), (SELECT itemID FROM inventory WHERE name = 'Raging Bull'), '1234')")
cursor.execute("INSERT INTO orders(total, quantity, userID, itemID, ccID) VALUES('4.34', '1', (SELECT userID FROM users WHERE username = 'c'), (SELECT itemID FROM inventory WHERE name = 'Casablanca'), '54321')")
cursor.execute("INSERT INTO orders(total, quantity, userID, itemID, ccID) VALUES('9.00', '2', (SELECT userID FROM users WHERE username = 'd'), (SELECT itemID FROM inventory WHERE name = 'The Shawshank Redemption'), '6780')")
cursor.execute("INSERT INTO orders(total, quantity, userID, itemID, ccID) VALUES('12.00', '2', (SELECT userID FROM users WHERE username = 'e'), (SELECT itemID FROM inventory WHERE name = 'Casablanca'), '5432')")
conn.commit();

#rows = cursor.execute("SELECT * FROM users WHERE username = ?", ('a',))
#pwd_context.verify('a', rows[0]["password"])
#print("Opened database successfully")

