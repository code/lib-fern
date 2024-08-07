using System.Text.Json.Serialization;

#nullable enable

namespace SeedTrace;

public record InitializeProblemRequest
{
    [JsonPropertyName("problemId")]
    public required string ProblemId { get; init; }

    [JsonPropertyName("problemVersion")]
    public int? ProblemVersion { get; init; }
}
