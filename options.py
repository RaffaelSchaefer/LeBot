from discord_slash.utils.manage_commands import create_option, create_choice

option_TruthOrDare = [
  create_option(
    name="mode",
    description="choose an entry based on mode selection",
    option_type=3,
    required=True,
    choices=[
      create_choice(
      name="Truth",
      value="truth"
    ),
      create_choice(
      name="Dare",
      value="dare"
    )
    ]
  )
]

option_eb = [
  create_option(
    name="question", description="The Question for the magic eight ball",option_type=3,required=True
  )
]

option_New = [
  create_option(
    name="mode",
    description="choose a mode",
    option_type=3,
    required=True,
    choices=[
      create_choice(
      name="Question",
      value="question"
    ),
      create_choice(
      name="Dare",
      value="dare"
    ),
      create_choice(
      name="Mostlikely",
      value="mostlikely"
    ),
      create_choice(
      name="Topics",
      value="topics"
    )
    ]
  ),
  create_option(
    name="input", description="The value of the entry",option_type=3,required=True
  )
]

option_del = [
  create_option(
    name="mode",
    description="choose a mode",
    option_type=3,
    required=True,
    choices=[
      create_choice(
      name="Question",
      value="question"
    ),
      create_choice(
      name="Dare",
      value="dare"
    ),
      create_choice(
      name="Mostlikely",
      value="mostlikely"
    ),
      create_choice(
      name="Topics",
      value="topics"
    )
    ]
  ),
  create_option(
    name="index", description="The index of the entry",option_type=4,required=True
  )
]

option_List = [
  create_option(
    name="mode",
    description="choose a mode",
    option_type=3,
    required=True,
    choices=[
      create_choice(
      name="Question",
      value="question"
    ),
      create_choice(
      name="Dare",
      value="dare"
    ),
      create_choice(
      name="Mostlikely",
      value="mostlikely"
    ),
      create_choice(
      name="Topics",
      value="topics"
    )
    ]
  )
]