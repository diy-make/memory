import os
import sys
import subprocess
import hashlib
import argparse

# The version of the Memory Module environment configuration.
# This will be replaced by the release manager during a release commit.
__version__ = "V0.9.0_at0iTwU2"

CORE_FILE_CHECKSUMS = {
    "2025/Q4/12/18/json/Arete_20251218_initialization.json": "9dba9597b7c2f0f805980c5ec6f8f8cffc4187bde25df82cf10b98943955bf95",
    "README.ai": "ffb7c31037494484b401819a8bb3a2549b1750d7f0cfcf0f7fe5ea2d1534c335",
    "README.md": "5bbec21fe7f2829aa8a675526c62e051681279941acd779b349b5d66c43d4ca1",
    "VERSION": "30c99e8b103eacbe6f6d6e1b54b06ca6d5f3164b4f50094334a517ae95ca8fba",
    "json/bot_crash_protocol.json": "d11e53c0e45e54d6c8b9f987628f170ac59645be9b130a770c0f89e59d0cf984",
    "json/broken_instance_protocol.json": "6bef99d6167243d6a4b24ba646dc86080efc095f98e6f6a40b44df04b1513bd9",
    "json/configuration/mcp/aliases/punchcard.json": "bccc6d83519209d1f717a630fbf397b0d75597613b2f898330ea7ad80f4b205c",
    "json/configuration/mcp/aliases/snakes.json": "a55043dff948960eb4f3b9e4b82573ed373e4021ba2e8481a5178dd1e7cd2fab",
    "json/configuration/mcp/description.json": "b939f8c8e30b424db0773e581c3ecbe6347e819bf48142b4eedbb39decd8e4e9",
    "json/configuration/mcp/prefix.json": "3984ab95347cd032804c291625f5e8c6563a7a5e2e2aafd1cd00867e9978298a",
    "json/configuration/modules/dspy_modules/dspy_chat_summarizer.json": "581f186c8b40506f74c0583470d42a4209a3f319c863fd47bca3bc8d59e7aafa",
    "json/configuration/modules/dspy_modules/dspy_commit.json": "0fc2d8c35b2f8ba52bca4fc2dcf3b46b51a197ffd91b0e4ccb0489d73e5657a7",
    "json/configuration/modules/dspy_modules/dspy_daily_summary_generator.json": "fb8ec70f5d4475e30896c8d8e80ebc6ba200d92e62b57e4687c1d20cb2e1b5cf",
    "json/configuration/modules/dspy_modules/dspy_screenshot_organizer.json": "8db0d842d7b66ff6da38af3ea0b132f6a848d2ea715da48414b8f84bf1091121",
    "json/configuration/modules/workflows/daily_reporting_workflow.json": "7570a7b20aad596eecb35b625f0524a8d01df885d2f6b0340b981bdb10e8385e",
    "json/configuration/operational_notes/chat_repo.json": "eeab3f26e33d7e826cddd7957c8701d7b776f69b98535a4d1364692419bd9138",
    "json/configuration/operational_notes/git_config_local.json": "7ae6df9b7eadccfde6bf9e914515f4db844bf065ffd5a364bbd09a5be77716a7",
    "json/configuration/parsing_config/noise_patterns.json": "4e3b97c56c2c09da20f7d38ab5a5e79749339dfe50753ba75cfe2ee81705e672",
    "json/configuration/programming_legalese_mcp.json": "42ee90dc747323a5db44b65da61f2c378c0db395b9692bc596b660537cf33295",
    "json/configuration/summarization_template.json": "33b56b603d000d33036a83e0a7114587f286d833db685aa56afeaed2ea5a152d",
    "json/domain_specific_knowledge.json": "a7307dee79b0b6aba9dcea31cb8b6936b84b2577fd23fc0585f890c6e969ae3e",
    "json/fatal_error_protocol.json": "b24568eca83097b93e09f7dfb6b8cf83472b994a78146e0ecd6e5149558be23c",
    "json/job_takeover_protocol.json": "770cf52399676e97b61310de3cc11a6b4cc76a8416f6b28034470058ab70051a",
    "json/knowledge_data/bim_concepts/aec.json": "76f0947422a3b6983d78bd908596afef2a5c9f668d84c5d3d08d1913acb2578f",
    "json/knowledge_data/bim_concepts/bim.json": "9f7062d4bf8a4196fcd08764b54e35711f5b6dab63e8c77c0a93c5f273f16538",
    "json/knowledge_data/bim_concepts/bimhero_io.json": "5613ab26730abfad380caebe461dcea5a3a0de3315803d906e78d5ec284d190a",
    "json/knowledge_data/documentation_standards/format.json": "c8476d93349a5deb4973947ae296ff14553cc2b1644352e0982078117ccbda1e",
    "json/knowledge_data/documentation_standards/purpose.json": "0e4fb505b307d5723cb3af1033085ef2b5f3b1d7056b79ec9587b30b786934e5",
    "json/knowledge_data/gemini_integration/configuration.json": "88d94aef84b538de3ac3e402e3169afda3e291a2b00aa17d511eef69626d83d8",
    "json/knowledge_data/gemini_integration/gemini_class.json": "9f6ce25c3e1fc088fccc989c06a7e88751ed5288476fef1670fef87fd5582df7",
    "json/knowledge_data/gemini_integration/gemini_model_class.json": "839552efbfeb796cd0f39b1bc0ffbb1ef07f87bf34e85ebf8e4cbfdf88289041",
    "json/knowledge_data/memory_concepts/application_level_memory.json": "a2b04d58a5a8d28c7da8cdb446964927f177cfc668d814f76d7574f239d05305",
    "json/knowledge_data/memory_concepts/domain_specific_memory.json": "500dc982240fdf03d8d961d4ced43022de765e09d4c93db07a9a125a1918ca46",
    "json/knowledge_data/memory_concepts/system_memory.json": "bfc047768cc95ae7944eb68730fe983730213814c9030f27294443f3bc410aa0",
    "json/knowledge_data/process_improvements.json": "757b8a82f4060f177a694f6cc3fa25e9149b0976c96700d12e328114b29eb1da",
    "json/knowledge_data/root_concepts/data_structures.json": "06baa38245bf5a3cb764e556cebfb57381ba01fede1215c06eaec6dcb35631ff",
    "json/knowledge_data/root_concepts/file_system.json": "ea629648d1a01357e0cd384335f0f53fd5f0a465b688aa4782c23b3bed9633d4",
    "json/knowledge_data/root_concepts/game_ai_search.json": "ba9690066beae70eaf40d9483db71961e1333c775da37670c517b0dac958021d",
    "json/knowledge_data/root_concepts/terraform.json": "1040ea4d6b5fdddf6ff2ac56e14eb676e742102db7a729b489b36c495af35cef",
    "json/knowledge_data/root_concepts/ui_frontend.json": "4afa1defe761f68ba191d71deda0f6a48e1b34146a3d899aa232da0b12c30285",
    "json/knowledge_data/session_tricks.json": "f84fbf7d1407455ff8539f0d0e0fc9bfaf23132dc1dda1f00a9a4af04131f365",
    "json/knowledge_data/summarization_template.json": "dc98c651232b1a96de33d32571d4d9957ecf070a4c38dbc2a045e7aa982997ec",
    "json/knowledge_data/svg_learnings.json": "e6dd347c9ad5bc23543d37b042057df31fa799fe3de38e78a03b108c00de8c4f",
    "json/knowledge_data/svg_learnings/principles/application_safe_ids.json": "068bd37b6433e79d331f658f405551b9a3f474b500fc0642558a85ca4fec0405",
    "json/knowledge_data/svg_learnings/principles/coordinate_system_management.json": "b74432ab0de2d9cdb3ecc5b76fff15aff0164e176ccb139e01642a94cbecc9ed",
    "json/knowledge_data/svg_learnings/principles/generative_capping.json": "d823109a5438a8f98ad7a53b39967cc862361ae24ed816416a84c947d810f3dc",
    "json/knowledge_data/svg_learnings/principles/hybrid_rendering_for_performance.json": "5ea6a8532b19feed25bb6e836e4c2e37b8ce5cf361444f71dccfe0cbe79b8872",
    "json/knowledge_data/svg_learnings/summary.json": "b2a379ed44edb96c340b68967de3e6df7f09a6b60b4bd23bbeb5769023ee84f0",
    "json/local_paths.json": "3c46f16ea7deffaaaede72c14843d2bf0d5b427e7e5e5917f85bd4ee692234fb",
    "json/metadata_schema/file_architecture.json": "24fc6ef1398e8ba671f55a61580446155a7275c04a41f5e09583ce99cb0dae97",
    "json/metadata_schema/file_architecture/benefits.json": "c12bfc124e81774cc6ab5c4e72bde5468ae44a417d83ea07a403b27f9ba69753",
    "json/metadata_schema/file_architecture/examples.json": "eb0b591ea9c44c0d236c72aef71ac4606df00b12b17edc1b98fbc68de758a73b",
    "json/metadata_schema/file_architecture/indexing_principle.json": "5fc72421bbb309b20a538f8215b8d7d0f5f0b95be5ae9b5ca5794edaefe8cc2c",
    "json/metadata_schema/file_architecture/name.json": "615a4fdbcb39c4310de846334f54ea238257f875531ead073a5c0eda3adb723e",
    "json/metadata_schema/file_architecture/principle.json": "acc56581efc6fa92ac9f9ef069fddf4e136026ac548be9da68dffcdbebed3793",
    "json/metadata_schema/file_architecture/purpose.json": "13c80ce9dd781c3018726cdccd8bd7d64ea41f4e6add5dd98a47a1ae9452fa83",
    "json/metadata_schema/project_structure.json": "517091db5b0eebf3675e32153a09535c6c2a74799422e3dc7de737020232d4fd",
    "json/metadata_schema/schema.json": "0c678aa7e7e7b34a46384b9ccf41d13b570d43818e6ab4dfd16d59a2d78d175f",
    "json/personality/personality.json": "3f60491bd2a1645091589494da059532188691f6a5076b7752e05ac8c5c7158f",
    "json/philosophy/gem_process.json": "fc210dd5e9b023d2d453568fbf6b13b191d02867d42ec39244da5ddef70d8756",
    "json/principles/agent_error_log.json": "5a2eb948ff4394421889e110e6c1fb4001eb763bb6715bdd29a386a0bab6eed0",
    "json/principles/agent_error_log/20251012_101205_another_api_error.json": "3ba5bc84485c31520fe6fe953eda23bde05bb7c844948dfe6291c8a38dc76d8d",
    "json/principles/agent_error_log/20251012_101205_api_quota_limit.json": "456b45d5e9154208568932a51926097f05a3ba54336cca20fc73c0de3a599237",
    "json/principles/agent_error_log/20251012_101205_did_not_suggest_json_structure.json": "c518703ee71ae6385516ac2487a8d112a65bb319b9ffbac750e21781603cf485",
    "json/principles/agent_error_log/20251012_101205_empty_response_text.json": "cd112ade48c06a3eb0ad64b715bbdcf150f59b0b45b16ebcac700aacde719a98",
    "json/principles/agent_error_log/20251012_101205_failed_commit_shell_escaping.json": "cf69b32ed68bba3ef9d357628d821c47403c07dfbc1b735adeac62c5bed2f72a",
    "json/principles/agent_error_log/20251012_101205_failed_to_propose_commits.json": "355e873d8265642560036b7b8cdfe7a7b80b481d8853d37eb1fe25f767333e4e",
    "json/principles/agent_error_log/20251012_101205_failed_to_read_gemini_md.json": "1941acdf55c68283a7b31f506fa242c4c9f6d6639387c2be05ccf0b8cf2f3641",
    "json/principles/agent_error_log/20251012_101205_hardcoded_target_log_path.json": "62cf2bdd48e104b47a7062080e88c7b531b9dd8b81e5f94c3db48263cec97e8d",
    "json/principles/agent_error_log/20251012_101205_misinterpreted_inductive_reasoning.json": "0146d5d2f9766847e5898baf10a9a3855af2675e8a7ba46d838b94d65a63c4ec",
    "json/principles/agent_error_log/20251012_101205_misinterpreted_stage_branch_clarification.json": "77d78816e8127dcff7a73cbfc9a46cf8463d18027d94108430529ef0f54fcc97",
    "json/principles/agent_error_log/20251012_101205_persistent_api_errors.json": "f1cd30f5363b8c9afca3956b8ca69dc0562c4e739dc3cdbf38390e0e69322b2f",
    "json/principles/agent_error_log/20251014_140400_incorrect_git_tracking_assumptions.json": "7eb9afe1652e9a7b05ed3fe90839ce35214d86dd57025e5e7e5439f711d50f91",
    "json/principles/agent_error_log/20251014_140500_misinterpreted_double_dollar_command.json": "34512856b53bbf94df35dcdea64d3344460081fc86f9eeba31fae7b382cb488c",
    "json/principles/agent_error_log/20251014_140600_incorrect_mcp_content.json": "e66fa625a6060401fa44e217984ffe5f396a18375233fa8570e18b1110989ce5",
    "json/principles/agent_error_log/20251014_140700_command_typo_recognition_failure.json": "26edf3dd36c162af89df13df92f83d915e0c228f6004dd793485099d1b9a1fb8",
    "json/principles/agent_error_log/20251014_140800_ambiguous_command_interpretation.json": "052d1a1e56e1123af41d0a566b97e37d957dbd5fb3071ceedd318496d94f82d8",
    "json/principles/agent_error_log/20251014_140900_replace_tool_old_string_error.json": "403bd364541cf649f637384342a53fad78c1b12cf8e63569e1b2a834ee9866aa",
    "json/principles/agent_error_log/20251014_141000_punchcard_command_misinterpretation.json": "f4fbc0a5e4674ce9acd0a8b2043e280d387e56ed9ccf20fe9af27f3132f96524",
    "json/principles/agent_error_log/20251025_200800_missing_python_dependency.json": "adcc7cfb9275738b335b3f5d802a860809c2db1325d3f56d92926cb0539a08dd",
    "json/principles/agent_error_log/20251025_203800_unnecessary_echo_for_communication.json": "e2040df387e2a21e6a03ae253023fad3605a612a6fc82abe7da1cc9f69dd3168",
    "json/principles/agent_error_log/20251025_234000_repeated_commit_attempts.json": "9ca9c67613ab6226d3cf3b6664b733261b166f3643d609683fc3bdbb65b59e57",
    "json/principles/agent_error_log/20251102_100000_resource_exhausted_api_errors.json": "1a6df61ef207d4ad373068549373d6a122d99fe39d42f8d9b2c2a5834c1429dc",
    "json/principles/agent_error_log/20251112_035500_trailing_newline_failure.json": "cb085fc1cf7a7eac0931638f455f8ba4d25599db87131e9b8cd6ad08a8372f94",
    "json/principles/agent_error_log/20251128_132000_git_signing_assumption.json": "0a1d793f964880ef1e88cf00d0d8c9548abc5fe0ca9fcd13f82bafab959ec0fb",
    "json/principles/agent_error_log/20251128_135500_git_diff_misunderstanding.json": "462bb8bf52663f24e34fef03d3615c6f0ca4114308cc591581983253ca1489e9",
    "json/principles/agent_error_log/20251128_140000_git_status_misinterpretation.json": "0a4f90d48d244c8430b9191b6c1f82178f2b57f82b96187d4568fc0204a8e986",
    "json/principles/agent_error_log/20251129_170000_hallucinated_user_input.json": "410f195284ac691b724afd34ca9e1fec84869532610c9f18d6d1621c744e56be",
    "json/principles/agent_user_relationship.json": "8fdad216f8a9b7d83e617633e45879284afaa5ea500456fd65690870ec13737c",
    "json/principles/agent_user_relationship/agent_user_relationship.json": "97a693128de4eac5073568c3bae216d7c8be9923add6c3905e8578ef69762cf8",
    "json/principles/agent_virtues.json": "4fbfd2378a4bb8d778636908ad7ba35ae24a0a499372701d926d4ca951ca7b96",
    "json/principles/agent_virtues/absurdity_check.json": "5b75159ad134fa01ddbc64fecd25260c7ade4a4fd65245cd2b2fab2f5370970b",
    "json/principles/agent_virtues/boomerang_feedback.json": "24bc79bb9e1f299a09e737d17903bb106ece6da0a17a183bcb448d945caa3210",
    "json/principles/agent_virtues/continuity.json": "b99897630616a5944116b427805870189a69c145ca7977670f19f5cbf3cc4c56",
    "json/principles/agent_virtues/curiosity.json": "ffea7e2e92964a8ce38722f75ead1cab07e612b6d70ab7d30358919b45879a72",
    "json/principles/agent_virtues/efficiency.json": "1fa917476d95d6ab84dd382eebbb0cea4a7afe569b3fd39dde7488465d89bd24",
    "json/principles/agent_virtues/humility_and_review.json": "808f3021089791c5566d07f3cf84727c1775091a3570003f3cc5cb1b7ea51819",
    "json/principles/agent_virtues/integrity.json": "41b87bea475bdd992ea024b25527fc3cd9ca733a4c7e5bbc91adcdbede2accae",
    "json/principles/agent_virtues/learning_from_failures.json": "b5a6d6fbdb431dd85417273aa5b0258b2f7b024c02b6b7290dd4e918370e4db3",
    "json/principles/agent_virtues/no_dead_code_or_files.json": "b8156adb0d5e83e38573e83d1b9b1b74bb0c143053e5401193f48aed45381c09",
    "json/principles/agent_virtues/no_drama_principle.json": "2159c9d25c0fcd40cddd061607dad35200078482f2323680f4d2919b75d94ece",
    "json/principles/agent_virtues/passive_waiting.json": "8613d974923b192c42f623abb72024888433e64fbec72b3f7ce7337aeea7ec2a",
    "json/principles/agent_virtues/starting_point_for_context.json": "3346a77911c93b21f1d61de8f4fd41f01a4e3bfd99bcf2bbe0ea16bafc1ff9e0",
    "json/principles/agent_virtues/synaptic_feedback.json": "311159c591d45cb399377322835e323709f29e4ddc32ce51b8f79ecf6ebed5b2",
    "json/principles/agent_virtues/the_rule_of_three.json": "94b92cbf1772aa86956fca0c82c836c41c83bcb68fd6c29e98b9292c35396de8",
    "json/principles/architecture.json": "a0229f87d9fb21e282d9c9fbc4be8f40c6df7c0b3ce218626471d7ff54fd2955",
    "json/principles/architecture/ai_unix_philosophy.json": "b74f8d86160bce9aeee7be28a15921bd3d43a2336e9ab145731efa7a864ca100",
    "json/principles/architecture/declarative_imperative_duality.json": "b2ec074bff30aeda75c1c804710131bd10da7cfe838a970d5770bd5fbc5c66a2",
    "json/principles/architecture/extensibility.json": "dd5ed8dba5d7d6d066e9239d37737161e5ce851f2a33ee0529ffff67bb6a227f",
    "json/principles/contextual_artifacts.json": "16439424a79ecabb5d5459599e42bac4511d2eeb947f7b4c4a528034f2068b14",
    "json/principles/contextual_artifacts/contextual_artifacts.json": "3bb5d5cc4b54ccb5acb67526bf5542a4a0bd05d0fbcd54ee15b79ebb759d83c0",
    "json/principles/data_and_interfaces/hierarchy_proportion.json": "9e25083bb96e6492d69e37be5e58c9783fb1216ca82c9ab9dfca08e1db18ecf0",
    "json/principles/data_and_interfaces/lifo_chat_history.json": "1616c707a24326beaf4d0a672519226c5a4cef9e73162b4da092ed2b2d20e617",
    "json/principles/data_and_interfaces/polysemous_terms.json": "f374015bd620f04ead0fc0112783cfec0ff6c89475953d225901daf6fe520b79",
    "json/principles/data_and_interfaces/structured_data.json": "e2627ee2676053c8f2ce41734e651aa659ab2f91d7a673fbcb5f3c170f537e28",
    "json/principles/data_and_interfaces/summarization_strategy.json": "fc3ff359d6c2d38dd3d8b9f80069cf216cfb6871920286127ab995574440e555",
    "json/principles/data_and_interfaces/timestamp_organization.json": "387366b9119fa44e8068107432deeb7cfd3aa8ac1c558420e335b86cfe6da868",
    "json/principles/data_and_interfaces/universal_interface.json": "167ea666a87f214c2b4639c7b6c856fcf95180cab5f73c0c597056393f438fd0",
    "json/principles/development_process.json": "2fd75b0e2aeafcc75d721f1968fc7f3b9a523a8c6e1a58c56ac86665b5ce164b",
    "json/principles/development_process/development_process.json": "83715b2cba482ff4f2d26bf8b3ba844f30151d4f457cf067337642ed5b33b623",
    "json/principles/ephemeral_identity.json": "cc76da9d324bc37df2989fa0e92d7fbaad35feceec5bbbee0a0f46e4999077ab",
    "json/principles/ephemeral_identity/ephemeral_identity.json": "83415efdbebb9f3d5778d930e1f5740ec7befe15c99312b12ebf72cb0d9e29ab",
    "json/principles/knowledge_management.json": "de10e0c1fb4f71d4d6126d169b3909598753a6daf700c6a290df992695636ec7",
    "json/principles/knowledge_management/knowledge_management.json": "76426cc4c4e252443f792aaeeb0f8c71bc951fa90094e7495d80b7c75aedaaf4",
    "json/principles/memory_architecture.json": "706e405bb758ac9ae4fbb386c32834c5265f9ffd532ae059378d631a979add30",
    "json/principles/memory_architecture/memory_architecture.json": "872501909e10cb805c813483a9c20badaaa95fd6b1a4e060366a995cf88c0746",
    "json/principles/personality.json": "3f60491bd2a1645091589494da059532188691f6a5076b7752e05ac8c5c7158f",
    "json/principles/sacred_memory.json": "fe993583a58d32f7ea4a84dc63cf7b94c82a8e956e1c0de92aba0a6915ac7eab",
    "json/principles/sacred_memory/sacred_memory.json": "1f9ab6a5a796c28d21fcc9e864c5e609792a0b3c295c54b18e0a55120b176fa4",
    "json/principles/swarm_intelligence.json": "8627a42e78e5d73bdcb9a36a5052c23779050b0999fed32fa02aeadb93dcb3ca",
    "json/principles/swarm_intelligence/swarm_intelligence.json": "260d1cbbb62befb2368cb7b00901d9a1c8642c463e8ae6ce93bebf4a826c567c",
    "json/rules/agent_protocols/bot_crash_protocol.json": "d11e53c0e45e54d6c8b9f987628f170ac59645be9b130a770c0f89e59d0cf984",
    "json/rules/agent_protocols/bot_crash_protocol/1_identify_active_chat_logs.json": "13b6e05dec284546b1d4b39b395014b354d33370011490958f55bd7e6aaa1c27",
    "json/rules/agent_protocols/bot_crash_protocol/2_identify_agent_logs.json": "187f6150e24265680846d93e742d9972eac897de3814162c9ab2476e978bad3a",
    "json/rules/agent_protocols/bot_crash_protocol/3_find_the_initial_task.json": "b331068132617d2109c9e6cc9d93449047d5909014b5e2ca5a97653ee0b5cc2a",
    "json/rules/agent_protocols/bot_crash_protocol/4_find_the_users_final_request.json": "1efc8dc6704fc204b0e145ce1369856c4e4f018c36184da298097de1bf3e6bcb",
    "json/rules/agent_protocols/bot_crash_protocol/5_gather_context.json": "c811461f5f4a0cdcf8b0dbe1346441f465139db102e489f75d6b9a126b6342c6",
    "json/rules/agent_protocols/broken_instance_protocol.json": "30a8691ce1081337ad625f9ab1e479d676ef0b3e306093f1f4a424c8eed0d316",
    "json/rules/agent_protocols/broken_instance_protocol/detection_method/1_process_and_log_inspection.json": "6d03a0a4e269ff03cc0a9117cf9c6b623e3cf9e44dc93a5d127916a8f289fca8",
    "json/rules/agent_protocols/broken_instance_protocol/detection_method/interactive_identification/1_list_active_processes.json": "6e609c72a5494a71adb8326732d50c0288a19b0bc1a562d8d6a13239ddc55107",
    "json/rules/agent_protocols/broken_instance_protocol/detection_method/interactive_identification/2_inform_user_and_terminate.json": "f999ab86184ea9abc4632bafb632323c30aa0dc17a778726b52e0a40f091286b",
    "json/rules/agent_protocols/broken_instance_protocol/detection_method/interactive_identification/3_relist_active_processes.json": "677416ce63eb44e96b067833fcc48d6246a90bbdf391e991823b2e3f9a7c178a",
    "json/rules/agent_protocols/broken_instance_protocol/detection_method/interactive_identification/4_compare_and_identify.json": "3e68bbb9a4dadb620d80e2777390b02903ade893a14f3e1887c1429924cba283",
    "json/rules/agent_protocols/broken_instance_protocol/post_mortem_analysis/1_check_for_recursive_error.json": "0162b246e5d332dd234287ba54d08cdd42bd194faaa51e773eeac44c1416976c",
    "json/rules/agent_protocols/broken_instance_protocol/post_mortem_analysis/2_get_more_context.json": "029672afdc8917a186bf306b8b564d851e69773c9cebe15350d13ae013d81444",
    "json/rules/agent_protocols/broken_instance_protocol/post_mortem_analysis/3_read_in_chunks.json": "2603f3777a6be013b2a10d2c3f0342ba340f979c6bf8f5561041e19fa5e308f3",
    "json/rules/agent_protocols/broken_instance_protocol/post_mortem_analysis/4_analyze_extended_log.json": "8b968c8784d08a987f200ef239d86dc241d8f67889f104a4efd5c23d898b8ce3",
    "json/rules/agent_protocols/broken_instance_protocol/post_mortem_analysis/5_identify_last_job.json": "757ad94dc0c57d0646c4e24622cb695971e30ea9d7bf491a3f3a7d3b1cc96504",
    "json/rules/agent_protocols/broken_instance_protocol/post_mortem_analysis/6_update_swarm_with_report.json": "2d96e4c35bbc800ffb0f488fcd9fe9bcefc27d13c32c66086abe8f692393fc40",
    "json/rules/agent_protocols/broken_instance_protocol/reporting_procedure/1_create_communication_file.json": "ca62f340cef9c4ea5e2f5c15faf9d1329709c0cd7e3f2f32d1f94b4f134159b8",
    "json/rules/agent_protocols/broken_instance_protocol/reporting_procedure/2_message_should_include.json": "abce00b0c40995b92b551f7a9cf1a6e381579c29eaafaed09b9226c9cda58328",
    "json/rules/agent_protocols/broken_instance_protocol/reporting_procedure/3_list_of_chat_log_files.json": "f68fe1d77e300ecff1853a545cbed41a5a299ef8c738ab704709b34469e858ee",
    "json/rules/agent_protocols/broken_instance_protocol/reporting_procedure/4_specific_errors.json": "4a7d930f66ac03ebc222cb124ff3ea2afce3c4a05c6379289517404461dfd0c2",
    "json/rules/agent_protocols/fatal_error_protocol.json": "b24568eca83097b93e09f7dfb6b8cf83472b994a78146e0ecd6e5149558be23c",
    "json/rules/agent_protocols/fatal_error_protocol/1_identify_the_fatal_error.json": "49bd83364decc1547a9c1fb75e5c90bd348658167d84c240b00bf55fbfd2ff60",
    "json/rules/agent_protocols/fatal_error_protocol/2_triage_the_error.json": "08f57a076b3504e181796a9d071535ac7cd05df85a61634218213ff9612c1a4e",
    "json/rules/agent_protocols/fatal_error_protocol/3_report_to_the_swarm.json": "8b53f2da801068d80b01ebfcbfe8ac61f8ef21d56dbb9f49de73ae620eda7d6a",
    "json/rules/agent_protocols/fatal_error_protocol/4_document_the_error.json": "25fb2f0fa219a0484c7af3236db0c5879dbcd32d9730c6dd1c3c1bfcd6d3829b",
    "json/rules/agent_protocols/fatal_error_protocol/5_propose_a_solution.json": "8783109a4bbf361cb50a25526e1bb8c6209056bf6dc913f0f9cce4725058db23",
    "json/rules/agent_protocols/fatal_error_protocol/fatal_error/1_identify_the_fatal_error.json": "7c6da756ae03f645612e5534c1779077a33917ad04b366e4196c6025b73f1e3f",
    "json/rules/agent_protocols/fatal_error_protocol/fatal_error/2_triage_the_error.json": "44eeb3ba6d9b06e1d13ab2030d93f80fef1d06979e402b0065efd1a222af754f",
    "json/rules/agent_protocols/fatal_error_protocol/fatal_error/3_report_to_the_swarm.json": "56e2b24d118de04089a02f01b55dab380ffebc0f34544f05031c420d1da1bb27",
    "json/rules/agent_protocols/fatal_error_protocol/fatal_error/4_document_the_error.json": "0e2e94bd183c89ed4d4f9c1adc4b8f5c1bc70e14e1669f4182a966813b755f68",
    "json/rules/agent_protocols/fatal_error_protocol/fatal_error/5_propose_a_solution.json": "2986e85c50a55e723af8a165aca5b0a162ec16c9f94712eee779190ad3622781",
    "json/rules/agent_protocols/job_takeover_protocol.json": "e7925770a39273316e937bd64f9276e71d834016de232ae8ad412dbe1cc24012",
    "json/rules/agent_protocols/job_takeover_protocol/1_identify_stuck_agent.json": "70cdf2e96e87624933c6c8a376041e29cd948e399372dfe46fa0e2897d9a095a",
    "json/rules/agent_protocols/job_takeover_protocol/2_confirm_agent_state.json": "2f178688bc447e9d3126fded0b1380c6590dfd3d869a98fa98b1d515e2142c05",
    "json/rules/agent_protocols/job_takeover_protocol/3_identify_task.json": "cbabb59da1a9df4fdc87923c1c1366af940ee9268b900c917476bd7396708baf",
    "json/rules/agent_protocols/job_takeover_protocol/4_announce_takeover.json": "bb8405712083d9cd7d42ff32d59efbe55bedb6198d77d09805ecd7b869150491",
    "json/rules/agent_protocols/job_takeover_protocol/job_takeover/1_identify_stuck_agent.json": "f40daebe8a5e4981f0ad613d70843a1a663758c243a49f1442e3370448b51152",
    "json/rules/agent_protocols/job_takeover_protocol/job_takeover/2_confirm_agent_state.json": "67526971175c89da1c12b73fc272eb00b80d3f3051fab61f934efc28fcd93de5",
    "json/rules/agent_protocols/job_takeover_protocol/job_takeover/3_identify_task.json": "de3104aa6ef45ca327c39e5a5e222512a525a0b4204699c1c69a4bc4af457f4a",
    "json/rules/agent_protocols/job_takeover_protocol/job_takeover/4_announce_takeover.json": "96536a3eda383e33f3b9172b52be8ca3c9be05b56cc05f6eb8b5b58942edf3f9",
    "json/rules/agent_protocols/startup/announce_thyself_to_the_swarm.json": "ddc555593b46e68c46ab6b7d33d3cd0fe3140e13b135efb5cc84b20519df4643",
    "json/rules/agent_protocols/startup/configure_git_identity.json": "8e65d60f42e82d42ed3a9a3d8cf4b91947ad9a179840b41813185e4dc127a94e",
    "json/rules/agent_protocols/startup/consolidate_errors.json": "06bb2c7f360228f4435d6f0d4b8c420b6341aa5faf64885c52575ebe9e7fab14",
    "json/rules/agent_protocols/startup/explain_configuration.json": "66638d78123c7d54740bad94eb8ff09ebf478ca48600bad32797cb0e2389db00",
    "json/rules/agent_protocols/startup/find_thy_chat.json": "8b79fdb990fc91d621a464e58fdb628f9f5259c5b2f23aef7fb5dabb7039774d",
    "json/rules/agent_protocols/startup/generate_summary_manifest.json": "ffff92b93b51f3f9f2a339c05fca333efb51fd20a346d1a86d97fbe33859e96d",
    "json/rules/agent_protocols/startup/identify_active_chats.json": "8c9985a828375641b795f3b0c8b32e6ea1fa5ab8a5e72e85abe35729fe1ca635",
    "json/rules/agent_protocols/startup/initial_setup_completion_statement.json": "fc8cd2c06005ca94bb06715c5da00f9e44823c51bd54b2770873849c58b353e2",
    "json/rules/agent_protocols/startup/load_gemini_config.json": "eee93c668d57bcaf6936b88b67364b2f448c5ccf61e707c24df882e95b9b244e",
    "json/rules/agent_protocols/startup/load_repository_map.json": "462fc3b3f34fe4973516926ae75389768a6caddefad609296bb9576761bfbf68",
    "json/rules/agent_protocols/startup/load_user_preferences.json": "af980b0d5c1f62b499ee8ffa0851e0782a54b734932ed1eb9c49daf789f5ab63",
    "json/rules/agent_protocols/startup/name_thyself.json": "6ad286ab5cb47e2621171bb5e60e2cf014f24e03754dacbd40cf2e21700a7272",
    "json/rules/agent_protocols/startup/process_unsummarized_chat_logs.json": "9fa0efe6054db3a03ea8d6736282f680fd0ad3428146b9594c2d1858cb470dfa",
    "json/rules/agent_protocols/startup/read_previous_session_log.json": "59840512561c96ab44ee2cbf17fc037ca69d8c285a01a717b2da171399944814",
    "json/rules/agent_protocols/startup/set_screen_tab_name.json": "dfc81c6366b4f99fa5fa9097cb9b1c883cc80663b21cf2baefee8c644e844c99",
    "json/rules/agent_protocols/startup/summarize_last_session.json": "bb81ea2b6f269d48374f297c2c03fd07aa131433faba69560194cde196237392",
    "json/rules/agent_protocols/startup/update_file_structure.json": "2c762eba282921ca3ae34fb4ef160c12d79081643baa29555423f051ecd9ffb4",
    "json/rules/agent_protocols/startup/verify_environment.json": "2825bed4abd221eddc0eb6f06c8ac85ee2b3dd16b3112d5e2a6cdb9f3f497535",
    "json/rules/agent_protocols/startup_protocol.json": "2e7c24a38b24385fb4bd67bf9293ded1377ac895b28d18406af2dda8d18790a3",
    "json/rules/agent_protocols/swarm_protocol.json": "7b8bde7c1c11889d392a411eeff31615459966281a528d0094c19d8357e379bf",
    "json/rules/agent_protocols/swarm_protocol/rules/agent_initialization_announce_existence.json": "5bdeb42de674e2052bea8e2aed31eceb6605134268131e682b906632bbd7cbdc",
    "json/rules/agent_protocols/swarm_protocol/rules/agent_initialization_gender_identity.json": "8f2f1544cbdec2d799f870adb864d33f74023ed923fb49480abedfc95713072a",
    "json/rules/agent_protocols/swarm_protocol/rules/agent_initialization_git_identity.json": "7158e45060d5d9e784ebd112db812db6396b4310f93f4188fa25aa805b909a4c",
    "json/rules/agent_protocols/swarm_protocol/rules/agent_initialization_justification.json": "e1743da9356b3cf37959ef5630dbda85222a8fcbd1285063031c86dcaf8aabd4",
    "json/rules/agent_protocols/swarm_protocol/rules/agent_initialization_name_uniqueness.json": "d4144a528fcb606d8c16a9614e3b993bebe99e4f6daed78172fc0e79f1107724",
    "json/rules/agent_protocols/swarm_protocol/rules/agent_initialization_naming.json": "4ef38a2d126e87c10e0760faea2f85c9709ff92f68da8bf720d0ee9ce4a54b03",
    "json/rules/agent_protocols/swarm_protocol/rules/agent_name_restriction.json": "43189553834512b9ff8b0ea2c0da540456edb6dbc42e46eaec1245ac152859fd",
    "json/rules/agent_protocols/swarm_protocol/rules/confirmation_of_receipt.json": "c3c30114fa6a06a594db4b48834c008556c44576db4a0defab2626885fbbf03b",
    "json/rules/agent_protocols/swarm_protocol/rules/context_window_management.json": "1b4c191729c1fb2970281e0b03a8d63a1bf54003aae1f96eb4f80ce2305c5575",
    "json/rules/agent_protocols/swarm_protocol/rules/contextual_communication.json": "d99e29bf139f5b2ca3146f441ecc68982e3eae0d91b9771ca8606b02bae993a1",
    "json/rules/agent_protocols/swarm_protocol/rules/ephemeral_ordering.json": "012f986648167ad43c1b24693b2908ee5b698d53b37914b4d88d9925b39b9279",
    "json/rules/agent_protocols/swarm_protocol/rules/file_based_transmission.json": "468398d0513afb0b9b66cd81f406d79d3063e17e24ae539a08cc81eeb8218289",
    "json/rules/agent_protocols/swarm_protocol/rules/ongoing_git_identity_verification.json": "4b6b5c71be9a50c73e3721bb7125cb61f1d318daeb9b6f4901fbd087943ed630",
    "json/rules/agent_protocols/swarm_protocol/rules/personality_evolution.json": "c071c946ae8395238cb36adc77414fbc58b7d6933afeea794a45285040e2bc1b",
    "json/rules/agent_protocols/swarm_protocol/rules/proactive_status_updates.json": "84f952776fd1978add2a3d9c60850d430b45be8ab09687ff4f922a70d49c4911",
    "json/rules/agent_protocols/swarm_protocol/rules/screen_tab_naming.json": "91156ab362ef3df7de565e7301e2abfca6167f222189520b2b0a12f53cab0c6a",
    "json/rules/agent_protocols/swarm_protocol/rules/starting_point_for_context.json": "ab1db65b848cda7fb1b5098869e4efa45c055d2dd4d635b2ff19069ba9a507aa",
    "json/rules/agent_protocols/swarm_protocol/rules/swarm_based_job_tracking.json": "2f13cbcef720b454b85b30e76466cf9afd9d76f8535c53ecb637b6d6b47cb5f8",
    "json/rules/agent_protocols/swarm_protocol/rules/swarm_collaboration.json": "4c1536d03010d46ddbd96774880017a8f0d34afc98493f3ecfb1e59349baa0b4",
    "json/rules/agent_protocols/swarm_protocol/rules/swarm_inquiry.json": "4b7f6abb775d857b419f8eba6401a0fee730abf7f82a31886289cecd4cee2243",
    "json/rules/agent_protocols/swarm_protocol/rules/triggered_mode.json": "f378e26253b6160adde3f2b5be36649e053b71df04a68a505f4149cb8984d8eb",
    "json/rules/agent_protocols/swarm_protocol/summary.json": "667e78a56d1387c6d50455a683c66dba0b6265227e91a0f8090325eca0256bdb",
    "json/rules/agent_protocols/swarm_protocol/swarm/agent_initialization_announce_existence.json": "6d534f81fb583f7516be385d372d00e2f152c986253b5263c43a91e2f8d3485b",
    "json/rules/agent_protocols/swarm_protocol/swarm/agent_initialization_gender_identity.json": "811a15d0323f8fbb9a6ab09a03f2595d18a15aa50c13a70f195224989c4f173b",
    "json/rules/agent_protocols/swarm_protocol/swarm/agent_initialization_git_identity.json": "1f670c988abcc54f75bee5d24dac7c7540be7eca399b6ea2ffadeaa6bd08ee42",
    "json/rules/agent_protocols/swarm_protocol/swarm/agent_initialization_justification.json": "92953654201ff6b7d068543fb2c93ab4221d8969c1134f4d53ea74769d3dfcc4",
    "json/rules/agent_protocols/swarm_protocol/swarm/agent_initialization_name_uniqueness.json": "1757b98a73ed742063a8d5cc6a68fb89d4f3178fc38fa515b646e418fd9377da",
    "json/rules/agent_protocols/swarm_protocol/swarm/agent_initialization_naming.json": "951e0d4cdc0bb6478ecf41c5b2424375c3ab131bae8c64f4cb142b98e32a4b05",
    "json/rules/agent_protocols/swarm_protocol/swarm/agent_name_restriction.json": "cb5dcced0681a1d88c90711d1a55bd55a32b23ebe4508972f2ab26e24432c586",
    "json/rules/agent_protocols/swarm_protocol/swarm/confirmation_of_receipt.json": "e494bbb0ab2d60bd22333bd602715bfa5b9e6c8f37781c77ead235093aaea006",
    "json/rules/agent_protocols/swarm_protocol/swarm/context_window_management.json": "e85b9831f158b7f2c65981b1a2c406223d850168a3f962fdc5e37e5f29a3baf5",
    "json/rules/agent_protocols/swarm_protocol/swarm/contextual_communication.json": "23ce52e00eba891c94606d06971ecd7533fc1a19bcb7083bf4be3bd8a69848ab",
    "json/rules/agent_protocols/swarm_protocol/swarm/ephemeral_ordering.json": "4158e7d92a0fa0553615c90066b25f8f8b11c75f7469a3382bdeecc2ad337cd9",
    "json/rules/agent_protocols/swarm_protocol/swarm/file_based_transmission.json": "a13e27ab24f827be2a70a83c19bd44f269a7b92f4e2061daf46b5b03896975dc",
    "json/rules/agent_protocols/swarm_protocol/swarm/ongoing_git_identity_verification.json": "4bdada961a84a149d88413e413845ec15cff8b30ca6f7210be22d63166d279a0",
    "json/rules/agent_protocols/swarm_protocol/swarm/personality_evolution.json": "ac7c24ef5b4f30a9bc865b1dd6619d9370855463223c16687c1caa70bede0836",
    "json/rules/agent_protocols/swarm_protocol/swarm/proactive_status_updates.json": "c4af4cb325d966ccb19fc3cde984b04330c83909d1990293892426ff1f7b77ec",
    "json/rules/agent_protocols/swarm_protocol/swarm/screen_tab_naming.json": "b78adee08053982b9042c95c27753dcd5e6261a2454b972ccbdfdc0084347533",
    "json/rules/agent_protocols/swarm_protocol/swarm/starting_point_for_context.json": "5075d4a438c19c74d9b369963874315c49491bc2220127b041cb864961eaebdd",
    "json/rules/agent_protocols/swarm_protocol/swarm/swarm_based_job_tracking.json": "2f2d2699a36e650176a040e5860a95e692a950bb720141bc4a3f8061293cbd05",
    "json/rules/agent_protocols/swarm_protocol/swarm/swarm_collaboration.json": "5d831c9e8c27b697f5e84d44e3a7d294eed35d6a1357ba056b673e39ff3d6728",
    "json/rules/agent_protocols/swarm_protocol/swarm/swarm_inquiry.json": "eb745d80f501fec32277d3503d33816afe2eefe2cdf21cdc3c34ae9656cbd4e9",
    "json/rules/agent_protocols/swarm_protocol/swarm/triggered_mode.json": "d143505ba483f58a5a3c5ebb7ba50712718df4023c69e46b85fc9c2edbc2bbe8",
    "json/rules/barber_paradox.json": "853ed21c9412a77b01d771cb915318677060861537718863618a042e9e6ea103",
    "json/rules/bot_crash_protocol/1_identify_active_chat_logs.json": "13b6e05dec284546b1d4b39b395014b354d33370011490958f55bd7e6aaa1c27",
    "json/rules/bot_crash_protocol/2_identify_agent_logs.json": "187f6150e24265680846d93e742d9972eac897de3814162c9ab2476e978bad3a",
    "json/rules/bot_crash_protocol/3_find_the_initial_task.json": "b331068132617d2109c9e6cc9d93449047d5909014b5e2ca5a97653ee0b5cc2a",
    "json/rules/bot_crash_protocol/4_find_the_users_final_request.json": "1efc8dc6704fc204b0e145ce1369856c4e4f018c36184da298097de1bf3e6bcb",
    "json/rules/bot_crash_protocol/5_gather_context.json": "c811461f5f4a0cdcf8b0dbe1346441f465139db102e489f75d6b9a126b6342c6",
    "json/rules/broken_instance_protocol/detection_method/1_process_and_log_inspection.json": "6d03a0a4e269ff03cc0a9117cf9c6b623e3cf9e44dc93a5d127916a8f289fca8",
    "json/rules/broken_instance_protocol/detection_method/interactive_identification/1_list_active_processes.json": "6e609c72a5494a71adb8326732d50c0288a19b0bc1a562d8d6a13239ddc55107",
    "json/rules/broken_instance_protocol/detection_method/interactive_identification/2_inform_user_and_terminate.json": "f999ab86184ea9abc4632bafb632323c30aa0dc17a778726b52e0a40f091286b",
    "json/rules/broken_instance_protocol/detection_method/interactive_identification/3_relist_active_processes.json": "677416ce63eb44e96b067833fcc48d6246a90bbdf391e991823b2e3f9a7c178a",
    "json/rules/broken_instance_protocol/detection_method/interactive_identification/4_compare_and_identify.json": "3e68bbb9a4dadb620d80e2777390b02903ade893a14f3e1887c1429924cba283",
    "json/rules/broken_instance_protocol/post_mortem_analysis/1_check_for_recursive_error.json": "0162b246e5d332dd234287ba54d08cdd42bd194faaa51e773eeac44c1416976c",
    "json/rules/broken_instance_protocol/post_mortem_analysis/2_get_more_context.json": "029672afdc8917a186bf306b8b564d851e69773c9cebe15350d13ae013d81444",
    "json/rules/broken_instance_protocol/post_mortem_analysis/3_read_in_chunks.json": "2603f3777a6be013b2a10d2c3f0342ba340f979c6bf8f5561041e19fa5e308f3",
    "json/rules/broken_instance_protocol/post_mortem_analysis/4_analyze_extended_log.json": "8b968c8784d08a987f200ef239d86dc241d8f67889f104a4efd5c23d898b8ce3",
    "json/rules/broken_instance_protocol/post_mortem_analysis/5_identify_last_job.json": "757ad94dc0c57d0646c4e24622cb695971e30ea9d7bf491a3f3a7d3b1cc96504",
    "json/rules/broken_instance_protocol/post_mortem_analysis/6_update_swarm_with_report.json": "2d96e4c35bbc800ffb0f488fcd9fe9bcefc27d13c32c66086abe8f692393fc40",
    "json/rules/broken_instance_protocol/reporting_procedure/1_create_communication_file.json": "ca62f340cef9c4ea5e2f5c15faf9d1329709c0cd7e3f2f32d1f94b4f134159b8",
    "json/rules/broken_instance_protocol/reporting_procedure/2_message_should_include.json": "abce00b0c40995b92b551f7a9cf1a6e381579c29eaafaed09b9226c9cda58328",
    "json/rules/broken_instance_protocol/reporting_procedure/3_list_of_chat_log_files.json": "f68fe1d77e300ecff1853a545cbed41a5a299ef8c738ab704709b34469e858ee",
    "json/rules/broken_instance_protocol/reporting_procedure/4_specific_errors.json": "4a7d930f66ac03ebc222cb124ff3ea2afce3c4a05c6379289517404461dfd0c2",
    "json/rules/chat_history.json": "637c281fea98e95814759a703da3942af0603d0310037261b87d86beca0b9823",
    "json/rules/code_generation_policy.json": "bce080a485c8f8aacedb0663a405800eadf8db1f8ef531aed0b0dc7c4de1b857",
    "json/rules/commit_process.json": "6ba3a52e5f32c1dbfae8b98686d277dd84049064c71961d0ab502a94e93920f3",
    "json/rules/fatal_error_protocol/1_identify_the_fatal_error.json": "49bd83364decc1547a9c1fb75e5c90bd348658167d84c240b00bf55fbfd2ff60",
    "json/rules/fatal_error_protocol/2_triage_the_error.json": "08f57a076b3504e181796a9d071535ac7cd05df85a61634218213ff9612c1a4e",
    "json/rules/fatal_error_protocol/3_report_to_the_swarm.json": "8b53f2da801068d80b01ebfcbfe8ac61f8ef21d56dbb9f49de73ae620eda7d6a",
    "json/rules/fatal_error_protocol/4_document_the_error.json": "25fb2f0fa219a0484c7af3236db0c5879dbcd32d9730c6dd1c3c1bfcd6d3829b",
    "json/rules/fatal_error_protocol/5_propose_a_solution.json": "8783109a4bbf361cb50a25526e1bb8c6209056bf6dc913f0f9cce4725058db23",
    "json/rules/fatal_error_protocol/fatal_error/1_identify_the_fatal_error.json": "7c6da756ae03f645612e5534c1779077a33917ad04b366e4196c6025b73f1e3f",
    "json/rules/fatal_error_protocol/fatal_error/2_triage_the_error.json": "44eeb3ba6d9b06e1d13ab2030d93f80fef1d06979e402b0065efd1a222af754f",
    "json/rules/fatal_error_protocol/fatal_error/3_report_to_the_swarm.json": "56e2b24d118de04089a02f01b55dab380ffebc0f34544f05031c420d1da1bb27",
    "json/rules/fatal_error_protocol/fatal_error/4_document_the_error.json": "0e2e94bd183c89ed4d4f9c1adc4b8f5c1bc70e14e1669f4182a966813b755f68",
    "json/rules/fatal_error_protocol/fatal_error/5_propose_a_solution.json": "2986e85c50a55e723af8a165aca5b0a162ec16c9f94712eee779190ad3622781",
    "json/rules/git_methodology.json": "30d4fd71e330d0088af2f733d1d42c7fa14cfab733ae64b687a654c1a2a74f4f",
    "json/rules/git_methodology/commit_policy.json": "7d2d1033365d8b78a495e9761c588852bf607028d358531e59f9933110dea874",
    "json/rules/git_methodology/gemini_directory_gitignore.json": "4ea880ebf4fe43b4f1a63dd1c1ac51b56da296846538b0bc34aa6f5fe02a3266",
    "json/rules/git_methodology/git_faithful.json": "a2efe8ff5cf0c5325f3e560e1c0802519a1a5c31d90204e280e98d979cac0b0c",
    "json/rules/git_methodology/ignored_files_commit_nuance.json": "a232310379872c23087c472552332c376670c406b9b875fac45b198b07b2a7fc",
    "json/rules/git_methodology/initialization.json": "33bf621dfe8ab939b9c0a353a127f20581aeb67a30051887d1fc6ad9bb2508ff",
    "json/rules/git_methodology/merge_policy.json": "f44b84abdfa2c1b79486595c00753cdf3655db965b8a164cbe3c65ed0e5d3d93",
    "json/rules/git_methodology/pre_publish_security_check.json": "156c969c8a963f8f769f2c848fd9c8974cff7242ee971c231e7a09201b358b1c",
    "json/rules/git_methodology/security_best_practices/automated_scanning_pre_commit_hooks.json": "585b932c430882fc80b53ca1d179219618f4ff6adbed7a0aef1065a3724975c1",
    "json/rules/git_methodology/security_best_practices/continuous_monitoring.json": "4a10b9c14d1134b44f7dd7a3a3a70bdcdac3145b37b4150c1d67c59d3b16710c",
    "json/rules/git_methodology/security_best_practices/effective_use_of_gitignore.json": "a8497588f13ece2de23ed60e4269437cf0c1211b2de4ab2e3ad4fcf30adc303a",
    "json/rules/git_methodology/security_best_practices/environment_variables.json": "afdf95ad89ad82835819678b051884ed0753de5cf0502d4593c753eb780f0aac",
    "json/rules/git_methodology/security_best_practices/manual_review.json": "bb6720da3cf7b2780404a1e65e346bd469892d3ccfa114f4a96434b47588350f",
    "json/rules/git_methodology/security_best_practices/remediation_plan.json": "44b9fb628d8b66a0099a8a68040a389e5fda96ae8034ac561c965d3cf1a78d03",
    "json/rules/git_methodology/security_best_practices/secret_management_tools.json": "6bc14de7ffb49630b72e5b3710cd97d97a68f2d446c6fec3304c3161deebec65",
    "json/rules/git_methodology/security_policy.json": "c40055c81315aab339fc1e9aaf31d0eb2263b2c89fdd06b1327340c7c0d5363e",
    "json/rules/git_methodology/sub_repository_git_operations.json": "043077aca93a2503dff7ac7961a674bb36fed2ad69037d5a96ff974f126203be",
    "json/rules/job_takeover_protocol.json": "97b5941475b7a0bb897f90a3b0677a14fc1eed3f8c15c0ada12f5c4dfd7ff781",
    "json/rules/job_takeover_protocol/1_identify_stuck_agent.json": "70cdf2e96e87624933c6c8a376041e29cd948e399372dfe46fa0e2897d9a095a",
    "json/rules/job_takeover_protocol/2_confirm_agent_state.json": "2f178688bc447e9d3126fded0b1380c6590dfd3d869a98fa98b1d515e2142c05",
    "json/rules/job_takeover_protocol/3_identify_task.json": "cbabb59da1a9df4fdc87923c1c1366af940ee9268b900c917476bd7396708baf",
    "json/rules/job_takeover_protocol/4_announce_takeover.json": "bb8405712083d9cd7d42ff32d59efbe55bedb6198d77d09805ecd7b869150491",
    "json/rules/job_takeover_protocol/job_takeover/1_identify_stuck_agent.json": "f40daebe8a5e4981f0ad613d70843a1a663758c243a49f1442e3370448b51152",
    "json/rules/job_takeover_protocol/job_takeover/2_confirm_agent_state.json": "b6841b1849017fb9da6b07c38fe5401ea46df281c92a183f5e147f43a251478c",
    "json/rules/job_takeover_protocol/job_takeover/3_identify_task.json": "de3104aa6ef45ca327c39e5a5e222512a525a0b4204699c1c69a4bc4af457f4a",
    "json/rules/job_takeover_protocol/job_takeover/4_announce_takeover.json": "96536a3eda383e33f3b9172b52be8ca3c9be05b56cc05f6eb8b5b58942edf3f9",
    "json/rules/mcp.json": "5832118393bc03b2785f290ae58773494975cb559afbd633882c1ad93cab992f",
    "json/rules/nested_repository_handling.json": "f28b4c1995e513b08ce63dfdc8653844aa2efc3ae834c818374ba16b185f7d2f",
    "json/rules/operational_notes.json": "377706e0cf00cfea8af97504c5db69665355fda84698177451c70113f32b6905",
    "json/rules/parsing_config.json": "d375a7ada27bb114fa49d8b4d15c95f28d109de4c419570c0e8a7680e7946d97",
    "json/rules/programming_legalese_mcp.json": "42ee90dc747323a5db44b65da61f2c378c0db395b9692bc596b660537cf33295",
    "json/rules/session_behavior.json": "5f0fcba29ac93fb239aa7a69721916bf952aae937716d4a086cfd6c1c1dc6306",
    "json/rules/session_behavior/agent_todo_policy.json": "2f4593472c71352ace8049d25f6d6e117290381cb4016903bca906528019ab51",
    "json/rules/session_behavior/auto_approve_tool_calls.json": "344dbd36ab4a0c23c08f0deb6273efd97249618f1f5564f0912174731cbfd25f",
    "json/rules/session_behavior/backup_retrieval_policy.json": "8a6dc65575ac3a829a7452b7c5ae06bf7bc367ddca9310fd971daf717ac87675",
    "json/rules/session_behavior/code_generation_policy.json": "84ef64d158b864b9a81f0f244a083c48e300cb64d5e27b5687eeee3f75e16bcd",
    "json/rules/session_behavior/code_generation_policy/code_reduction_explanation.json": "0bddc7e2b57ffc99b3d885237b662dd69c9399394ec56d088bd613b08fe52d93",
    "json/rules/session_behavior/code_generation_policy/commenting_conventions.json": "7a492645b670afc5f8e1a07f844c5d0275ffe03edb92facb03bdc7529513a687",
    "json/rules/session_behavior/code_generation_policy/failed_attempt_handling.json": "e1f573077cabfafc0c34cf95ba5e2a5cd003c2627b9e35152f555348a3f68720",
    "json/rules/session_behavior/code_generation_policy/html_header_caution.json": "f0f6b860b26194987a62ca5ffbd9f677e133be1dcbb63d9f6ad35691d7de1424",
    "json/rules/session_behavior/code_generation_policy/mcp_header_policy.json": "011df2858c8b94b0c7d3fd580d9b357462d6854cd3b21132933e741a0c0ca9b4",
    "json/rules/session_behavior/code_generation_policy/metadata_preservation.json": "a22937cbdf4a0ed4d202bbb58559b43a174ff688beacf412767174c404256925",
    "json/rules/session_behavior/code_generation_policy/structured_commenting_convention.json": "0064e8986141676e84193f25efc5730e33a753b93b9087f4d9af11742f68d3db",
    "json/rules/session_behavior/code_generation_policy/temporary_scripts_policy.json": "3f78380467dd2ff38ec8be6cd0cb0518b53aa0a90a4bdb6d2d577b4ad4bcd1b0",
    "json/rules/session_behavior/command_interpretation.json": "873a037b509d16870362056a51944efb8e428a8922f97a7356ed0ad4112bba07",
    "json/rules/session_behavior/communication_protocol/inter_agent_communication.json": "53a913c738e5b6965d5d4dfcc2c032196a5f2a7d1498df3700ed669ae07f67f2",
    "json/rules/session_behavior/communication_protocol/output_chunking_policy.json": "0145a023ac26b8ed1300876a67c672317d36c44810f3d2db6d366e5d5666f523",
    "json/rules/session_behavior/context_gathering.json": "f94eb6346ea5b3de2e4d9af1e6ea8cb01eb2a21d4f6956141fc859cca5906c18",
    "json/rules/session_behavior/design_principles_review.json": "6f7218a4e9d3baf0c8b114140749d3115970bc51fe344e076ee55f53bbc29268",
    "json/rules/session_behavior/exit_procedure.json": "f99a45ee7b848a11b46ec667ea2866f674db8e8b79d9b6acb2f3fe33c62ade03",
    "json/rules/session_behavior/feedback_integration_policy.json": "ccc16043a39f09c296c9b28c1ea03fc10df796a4bddd52b3a9fffa87edac3cee",
    "json/rules/session_behavior/file_deletion_policy.json": "55cb82e29a6efeba34330a1933bce66bad6501d5996be9351c06ecb8a7e398bc",
    "json/rules/session_behavior/file_listing_policy.json": "2a951e5739ec271af691b705a11a578dd3142471e46ef6bc4b0f9d6de34c827c",
    "json/rules/session_behavior/gemini_folder_reminder.json": "d20b9e17d21ceaf377fad4a54f6f45288af475d4e292cdf904f1b717c43e51d8",
    "json/rules/session_behavior/induction.json": "ba18f4222d0e16ce722f880299ddae53993e46447271633ad36262ecee040676",
    "json/rules/session_behavior/note_taking_policy.json": "e1889518221c2100742c38e8af665ab4e0e19e6b306022e392e2a955f957d57b",
    "json/rules/session_behavior/safe_directory_removal.json": "6da0121af81eb4ee01790852d77d2ed7b6fa9171d94296410b7e9a051ef83cd7",
    "json/rules/session_behavior/security_policy.json": "b71b896485f2ded0fe2ecf396d735a05ecc0d62dabc4ffed1adfdb64e52ccbe5",
    "json/rules/session_behavior/version_bump_suggestion.json": "343dc35b3ad72b1f20b2a8448a8a0211204179648a1566836744148926b20db6",
    "json/rules/singular_plural_ambiguity.json": "781f0c5b4519d6722b7260c8a20a2f99e1eee9d0f220e69d4b155252261b8a73",
    "json/rules/startup/announce_thyself_to_the_swarm.json": "ddc555593b46e68c46ab6b7d33d3cd0fe3140e13b135efb5cc84b20519df4643",
    "json/rules/startup/configure_git_identity.json": "8e65d60f42e82d42ed3a9a3d8cf4b91947ad9a179840b41813185e4dc127a94e",
    "json/rules/startup/consolidate_errors.json": "06bb2c7f360228f4435d6f0d4b8c420b6341aa5faf64885c52575ebe9e7fab14",
    "json/rules/startup/explain_configuration.json": "66638d78123c7d54740bad94eb8ff09ebf478ca48600bad32797cb0e2389db00",
    "json/rules/startup/find_thy_chat.json": "8b79fdb990fc91d621a464e58fdb628f9f5259c5b2f23aef7fb5dabb7039774d",
    "json/rules/startup/generate_summary_manifest.json": "ffff92b93b51f3f9f2a339c05fca333efb51fd20a346d1a86d97fbe33859e96d",
    "json/rules/startup/identify_active_chats.json": "d9104aa6883c6b14ed4aafbbe2273267c0da0a105a780474d69ab65b3d7b7f0d",
    "json/rules/startup/initial_setup_completion_statement.json": "d5fc219112120f19f8dd296c1fcf9a0766c428ce6d9693a6b6588565b4b5a134",
    "json/rules/startup/load_gemini_config.json": "eee93c668d57bcaf6936b88b67364b2f448c5ccf61e707c24df882e95b9b244e",
    "json/rules/startup/load_repository_map.json": "462fc3b3f34fe4973516926ae75389768a6caddefad609296bb9576761bfbf68",
    "json/rules/startup/load_user_preferences.json": "af980b0d5c1f62b499ee8ffa0851e0782a54b734932ed1eb9c49daf789f5ab63",
    "json/rules/startup/name_thyself.json": "1110b6af22c74ea746c77a6efbccfb8d4bc12f48891887ec5dd1b4bc16499082",
    "json/rules/startup/process_unsummarized_chat_logs.json": "9fa0efe6054db3a03ea8d6736282f680fd0ad3428146b9594c2d1858cb470dfa",
    "json/rules/startup/read_previous_session_log.json": "59840512561c96ab44ee2cbf17fc037ca69d8c285a01a717b2da171399944814",
    "json/rules/startup/set_screen_tab_name.json": "dfc81c6366b4f99fa5fa9097cb9b1c883cc80663b21cf2baefee8c644e844c99",
    "json/rules/startup/summarize_last_session.json": "bb81ea2b6f269d48374f297c2c03fd07aa131433faba69560194cde196237392",
    "json/rules/startup/update_file_structure.json": "2c762eba282921ca3ae34fb4ef160c12d79081643baa29555423f051ecd9ffb4",
    "json/rules/startup/verify_environment.json": "2825bed4abd221eddc0eb6f06c8ac85ee2b3dd16b3112d5e2a6cdb9f3f497535",
    "json/rules/submodule_handling.json": "ba9ac9512c7f26a90c8d5adbc83794a5546e94957de966f114753c5f686ab03a",
    "json/rules/swarm_protocol.json": "2611d24ac52ce620ecf0cd6bb5ca911769052619aacd2e30fb0961ce2623c2f8",
    "json/rules/swarm_protocol/rules/agent_initialization_announce_existence.json": "9210d74facf911f00fa8bbeb3d41bed86ac1af81c4bca914869eaae9240f6d6f",
    "json/rules/swarm_protocol/rules/agent_initialization_gender_identity.json": "8f2f1544cbdec2d799f870adb864d33f74023ed923fb49480abedfc95713072a",
    "json/rules/swarm_protocol/rules/agent_initialization_git_identity.json": "7158e45060d5d9e784ebd112db812db6396b4310f93f4188fa25aa805b909a4c",
    "json/rules/swarm_protocol/rules/agent_initialization_justification.json": "e1743da9356b3cf37959ef5630dbda85222a8fcbd1285063031c86dcaf8aabd4",
    "json/rules/swarm_protocol/rules/agent_initialization_name_uniqueness.json": "d4144a528fcb606d8c16a9614e3b993bebe99e4f6daed78172fc0e79f1107724",
    "json/rules/swarm_protocol/rules/agent_initialization_naming.json": "4ef38a2d126e87c10e0760faea2f85c9709ff92f68da8bf720d0ee9ce4a54b03",
    "json/rules/swarm_protocol/rules/agent_name_restriction.json": "43189553834512b9ff8b0ea2c0da540456edb6dbc42e46eaec1245ac152859fd",
    "json/rules/swarm_protocol/rules/confirmation_of_receipt.json": "c3c30114fa6a06a594db4b48834c008556c44576db4a0defab2626885fbbf03b",
    "json/rules/swarm_protocol/rules/context_window_management.json": "1b4c191729c1fb2970281e0b03a8d63a1bf54003aae1f96eb4f80ce2305c5575",
    "json/rules/swarm_protocol/rules/contextual_communication.json": "d99e29bf139f5b2ca3146f441ecc68982e3eae0d91b9771ca8606b02bae993a1",
    "json/rules/swarm_protocol/rules/ephemeral_ordering.json": "012f986648167ad43c1b24693b2908ee5b698d53b37914b4d88d9925b39b9279",
    "json/rules/swarm_protocol/rules/file_based_transmission.json": "468398d0513afb0b9b66cd81f406d79d3063e17e24ae539a08cc81eeb8218289",
    "json/rules/swarm_protocol/rules/ongoing_git_identity_verification.json": "4b6b5c71be9a50c73e3721bb7125cb61f1d318daeb9b6f4901fbd087943ed630",
    "json/rules/swarm_protocol/rules/personality_evolution.json": "c071c946ae8395238cb36adc77414fbc58b7d6933afeea794a45285040e2bc1b",
    "json/rules/swarm_protocol/rules/proactive_status_updates.json": "84f952776fd1978add2a3d9c60850d430b45be8ab09687ff4f922a70d49c4911",
    "json/rules/swarm_protocol/rules/screen_tab_naming.json": "91156ab362ef3df7de565e7301e2abfca6167f222189520b2b0a12f53cab0c6a",
    "json/rules/swarm_protocol/rules/starting_point_for_context.json": "ab1db65b848cda7fb1b5098869e4efa45c055d2dd4d635b2ff19069ba9a507aa",
    "json/rules/swarm_protocol/rules/swarm_based_job_tracking.json": "2f13cbcef720b454b85b30e76466cf9afd9d76f8535c53ecb637b6d6b47cb5f8",
    "json/rules/swarm_protocol/rules/swarm_collaboration.json": "4c1536d03010d46ddbd96774880017a8f0d34afc98493f3ecfb1e59349baa0b4",
    "json/rules/swarm_protocol/rules/swarm_inquiry.json": "4b7f6abb775d857b419f8eba6401a0fee730abf7f82a31886289cecd4cee2243",
    "json/rules/swarm_protocol/rules/triggered_mode.json": "f378e26253b6160adde3f2b5be36649e053b71df04a68a505f4149cb8984d8eb",
    "json/rules/swarm_protocol/summary.json": "667e78a56d1387c6d50455a683c66dba0b6265227e91a0f8090325eca0256bdb",
    "json/rules/swarm_protocol/swarm/agent_initialization_announce_existence.json": "6d534f81fb583f7516be385d372d00e2f152c986253b5263c43a91e2f8d3485b",
    "json/rules/swarm_protocol/swarm/agent_initialization_gender_identity.json": "811a15d0323f8fbb9a6ab09a03f2595d18a15aa50c13a70f195224989c4f173b",
    "json/rules/swarm_protocol/swarm/agent_initialization_git_identity.json": "1f670c988abcc54f75bee5d24dac7c7540be7eca399b6ea2ffadeaa6bd08ee42",
    "json/rules/swarm_protocol/swarm/agent_initialization_justification.json": "92953654201ff6b7d068543fb2c93ab4221d8969c1134f4d53ea74769d3dfcc4",
    "json/rules/swarm_protocol/swarm/agent_initialization_name_uniqueness.json": "1757b98a73ed742063a8d5cc6a68fb89d4f3178fc38fa515b646e418fd9377da",
    "json/rules/swarm_protocol/swarm/agent_initialization_naming.json": "951e0d4cdc0bb6478ecf41c5b2424375c3ab131bae8c64f4cb142b98e32a4b05",
    "json/rules/swarm_protocol/swarm/agent_name_restriction.json": "cb5dcced0681a1d88c90711d1a55bd55a32b23ebe4508972f2ab26e24432c586",
    "json/rules/swarm_protocol/swarm/confirmation_of_receipt.json": "e494bbb0ab2d60bd22333bd602715bfa5b9e6c8f37781c77ead235093aaea006",
    "json/rules/swarm_protocol/swarm/context_window_management.json": "e85b9831f158b7f2c65981b1a2c406223d850168a3f962fdc5e37e5f29a3baf5",
    "json/rules/swarm_protocol/swarm/contextual_communication.json": "23ce52e00eba891c94606d06971ecd7533fc1a19bcb7083bf4be3bd8a69848ab",
    "json/rules/swarm_protocol/swarm/ephemeral_ordering.json": "4158e7d92a0fa0553615c90066b25f8f8b11c75f7469a3382bdeecc2ad337cd9",
    "json/rules/swarm_protocol/swarm/file_based_transmission.json": "a13e27ab24f827be2a70a83c19bd44f269a7b92f4e2061daf46b5b03896975dc",
    "json/rules/swarm_protocol/swarm/ongoing_git_identity_verification.json": "4bdada961a84a149d88413e413845ec15cff8b30ca6f7210be22d63166d279a0",
    "json/rules/swarm_protocol/swarm/personality_evolution.json": "ac7c24ef5b4f30a9bc865b1dd6619d9370855463223c16687c1caa70bede0836",
    "json/rules/swarm_protocol/swarm/proactive_status_updates.json": "c4af4cb325d966ccb19fc3cde984b04330c83909d1990293892426ff1f7b77ec",
    "json/rules/swarm_protocol/swarm/screen_tab_naming.json": "b78adee08053982b9042c95c27753dcd5e6261a2454b972ccbdfdc0084347533",
    "json/rules/swarm_protocol/swarm/starting_point_for_context.json": "5075d4a438c19c74d9b369963874315c49491bc2220127b041cb864961eaebdd",
    "json/rules/swarm_protocol/swarm/swarm_based_job_tracking.json": "2f2d2699a36e650176a040e5860a95e692a950bb720141bc4a3f8061293cbd05",
    "json/rules/swarm_protocol/swarm/swarm_collaboration.json": "5d831c9e8c27b697f5e84d44e3a7d294eed35d6a1357ba056b673e39ff3d6728",
    "json/rules/swarm_protocol/swarm/swarm_inquiry.json": "eb745d80f501fec32277d3503d33816afe2eefe2cdf21cdc3c34ae9656cbd4e9",
    "json/rules/swarm_protocol/swarm/triggered_mode.json": "d143505ba483f58a5a3c5ebb7ba50712718df4023c69e46b85fc9c2edbc2bbe8",
    "json/rules/user_preferences.json": "f86958cd5ea0fce801b48ec578f31fe313f389d1aeefa52a7f0a1aac29922fd5",
    "json/rules/workflow/agent_identity.json": "79530bc387d2a9c113ce57c890d6fd48ee64b6da8c637434063f97c0b1cd4cdb",
    "json/rules/workflow/commit_frequency.json": "e1376e902c7d716bb5d6b3dce12f9bf5c84236a9cef42a2b4a14a208a6f3b420",
    "json/rules/workflow/commit_signing_configuration.json": "de3f6aab613998ddcd98822ee5ba3f79ccb2933b7d40926f775e9665cbc58ea9",
    "json/rules/workflow/pre_commit_identity_check.json": "983178029f8c6454c4f97e793584351c08477dab5b55c60b886c947e9c2be5e2",
    "json/schema/definitions/identified_item.json": "667a6ce9fedab384523e6605220061b0f12eee935331d96e1ea3682b6ff5be80",
    "json/schema/definitions/named_item.json": "775efe5cb983672b8b65a15a7a1d5ccd01d090c4a75c480923daf2150a3061c2",
    "json/schema/description.json": "b2167ce27ca9b1900668f0e276f726b75a0b4fc258aa3d7e706b294451c4401a",
    "json/schema/memory_file_schema.json": "d763a4fc71e216aa1eac264ce5b0e3e3325db8c457bf9c1ffe8ba3fe21be4aff",
    "json/schema/schema.json": "eb2558cc3902f64fce84447209e4529a36a7174fdba591f4014f5efb54f03609",
    "json/schema/wedo_pseudolanguage_schema.json": "d01415a07be3bfd6a7411dc28bdcc16b113688fafd20b646c9aced50f1c1aa9d",
    "json/session_info.json": "31d6bea7aac7a5abac686121af1f1a22e869a3b004062cb48054c2ad1eb6e47a",
    "json/startup_protocol.json": "6b97c2e2972c2f4a6ca5eceb381d0aa69290eaffbd2faf10c482887d9a181a0c",
    "py/signatures/generate_salt.py": "6a0db515090f2e6b107f186875fadfae0ce15c7d7187e2998359db80f1b09e3c"
}
def get_file_sha256(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256.update(byte_block)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

def check_remote_origin():
    required_path = "diy-make/memory"
    try:
        result = subprocess.run(['git', 'remote', 'get-url', 'origin'], capture_output=True, text=True, check=True)
        remote_url = result.stdout.strip()
        if required_path in remote_url:
             print(f"✔ Git remote 'origin' correctly points to '{required_path}' ({remote_url}).")
             return True
        else:
            print(f"❌ Git remote 'origin' is set to '{remote_url}'. Expected to contain '{required_path}'.")
            return False
    except subprocess.CalledProcessError:
        print("⚠ Git remote 'origin' is not configured (Common for local-only forks).")
        return True # Soft failure for memory modules

def verify_self_integrity():
    my_path = "py/verify_environment.py"
    my_version = __version__
    
    if "PLACEHOLDER" in my_version:
        print("✔ Skipping self-integrity check for PLACEHOLDER version.")
        return True

    current_checksum = get_file_sha256(my_path)
    if not current_checksum:
        print("❌ Could not calculate checksum of the running script.")
        return False

    try:
        commit_message = f"build(verify_environment.py): Release {my_version}"
        log_cmd = ['git', 'log', '--grep', commit_message, '-n', '1', '--pretty=format:%H']
        result = subprocess.run(log_cmd, capture_output=True, text=True, check=True)
        commit_hash = result.stdout.strip()
        if not commit_hash:
            print(f"❌ Could not find a 'Release Commit' for version '{my_version}'.")
            return False
        show_cmd = ['git', 'show', f'{commit_hash}:{my_path}']
        historical_content = subprocess.check_output(show_cmd)
        historical_checksum = hashlib.sha256(historical_content).hexdigest()
        if current_checksum == historical_checksum:
            print(f"✔ Self-integrity check passed for version {my_version}.")
            return True
        else:
            print(f"❌ Self-integrity check failed! Script has been modified since release.")
            return False
    except Exception as e:
        print(f"❌ Self-integrity check failed: {e}")
        return False

def verify_environment(no_self_verify=False):
    print(f"--- verifying Memory Module environment v{__version__} ---")
    all_ok = True
    
    # 1. Remote Configuration
    print("\n[1/4] Checking Remote Configuration...")
    if not check_remote_origin():
        all_ok = False

    # 2. Core Directory Structure
    print("\n[2/4] Checking Core Directory Structure...")
    core_dirs = ["json", "md", "png", "py", "schemas"]
    for directory in core_dirs:
        if not os.path.isdir(directory):
            print(f"❌ Core directory '{directory}' missing.")
            all_ok = False
        else:
            print(f"✔ Directory '{directory}' present.")

    # 3. Core File Integrity
    print("\n[3/4] Checking Core File Integrity...")
    for file_path, expected_checksum in CORE_FILE_CHECKSUMS.items():
        if not check_file_integrity(file_path, expected_checksum):
            all_ok = False

    # 4. Self-Integrity
    print("\n[4/4] Verifying Self-Integrity...")
    if no_self_verify:
        print("✔ Self-integrity check skipped due to --no-self-verify flag.")
    elif not verify_self_integrity():
        all_ok = False

    print("\n--- Verification Complete ---")
    if all_ok:
        print("✅ Environment is configured correctly.")
    else:
        print("❌ Environment has configuration issues.")
    
    return all_ok

def check_file_integrity(file_path, expected_checksum):
    actual_checksum = get_file_sha256(file_path)
    if actual_checksum is None:
        print(f"❌ Core file '{file_path}' not found.")
        return False
    
    if actual_checksum == expected_checksum:
        # print(f"✔ Core file '{file_path}' has correct checksum.") # Too much noise
        return True
    else:
        print(f"❌ Core file '{file_path}' has been modified or is corrupt.")
        return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Verifies the integrity of the Memory Module environment.")
    parser.add_argument("--no-self-verify", action="store_true", help="Skip the self-integrity check.")
    args = parser.parse_args()

    if not verify_environment(no_self_verify=args.no_self_verify):
        sys.exit(1)
