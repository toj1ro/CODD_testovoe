--name: get_news
SELECT preview_url, title, publish_date FROM news WHERE publish_date >= :date ORDER BY publish_date DESC;