from crewai_tools import YoutubeChannelSearchTool

## initialize the tool with a specific Youtube channel handle to target your search
## yt_tool = YoutubeChannelSearchTool(youtube_channel_handle = '@krishnaik06')

## Configure the tool to use Ollama for both search embeddings and internal summaries
yt_tool = YoutubeChannelSearchTool(
    youtube_channel_handle = '@krishnaik06',
    config = dict(
        llm = dict(
            provider = "ollama",
            config = dict(
                model = "gemma2:2b",
            ),
        ),
        embedder = dict(
            provider = "ollama",
            config = dict(
                model = "nomic-embed-text",
            ),
        ),
    )
)
