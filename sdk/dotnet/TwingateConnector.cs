// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Emailbob.Twingate
{
    /// <summary>
    /// Connectors provide connectivity to Remote Networks. This resource type will create the Connector in the Twingate Admin Console, but in order to successfully deploy it, you must also generate Connector tokens that authenticate the Connector with Twingate. For more information, see Twingate's [documentation](https://docs.twingate.com/docs/understanding-access-nodes).
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Twingate = Emailbob.Twingate;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var awsNetwork = new Twingate.TwingateRemoteNetwork("awsNetwork");
    /// 
    ///     var awsConnector = new Twingate.TwingateConnector("awsConnector", new()
    ///     {
    ///         RemoteNetworkId = awsNetwork.Id,
    ///         StatusUpdatesEnabled = true,
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// ```sh
    /// $ pulumi import twingate:index/twingateConnector:TwingateConnector aws_connector Q29ubmVjdG9yOjI2NzM=
    /// ```
    /// </summary>
    [TwingateResourceType("twingate:index/twingateConnector:TwingateConnector")]
    public partial class TwingateConnector : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Name of the Connector, if not provided one will be generated.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The ID of the Remote Network the Connector is attached to.
        /// </summary>
        [Output("remoteNetworkId")]
        public Output<string> RemoteNetworkId { get; private set; } = null!;

        /// <summary>
        /// Determines whether status notifications are enabled for the Connector. Default is `true`.
        /// </summary>
        [Output("statusUpdatesEnabled")]
        public Output<bool> StatusUpdatesEnabled { get; private set; } = null!;


        /// <summary>
        /// Create a TwingateConnector resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public TwingateConnector(string name, TwingateConnectorArgs args, CustomResourceOptions? options = null)
            : base("twingate:index/twingateConnector:TwingateConnector", name, args ?? new TwingateConnectorArgs(), MakeResourceOptions(options, ""))
        {
        }

        private TwingateConnector(string name, Input<string> id, TwingateConnectorState? state = null, CustomResourceOptions? options = null)
            : base("twingate:index/twingateConnector:TwingateConnector", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/emailbob/pulumi-twingate",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing TwingateConnector resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static TwingateConnector Get(string name, Input<string> id, TwingateConnectorState? state = null, CustomResourceOptions? options = null)
        {
            return new TwingateConnector(name, id, state, options);
        }
    }

    public sealed class TwingateConnectorArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Name of the Connector, if not provided one will be generated.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the Remote Network the Connector is attached to.
        /// </summary>
        [Input("remoteNetworkId", required: true)]
        public Input<string> RemoteNetworkId { get; set; } = null!;

        /// <summary>
        /// Determines whether status notifications are enabled for the Connector. Default is `true`.
        /// </summary>
        [Input("statusUpdatesEnabled")]
        public Input<bool>? StatusUpdatesEnabled { get; set; }

        public TwingateConnectorArgs()
        {
        }
        public static new TwingateConnectorArgs Empty => new TwingateConnectorArgs();
    }

    public sealed class TwingateConnectorState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Name of the Connector, if not provided one will be generated.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the Remote Network the Connector is attached to.
        /// </summary>
        [Input("remoteNetworkId")]
        public Input<string>? RemoteNetworkId { get; set; }

        /// <summary>
        /// Determines whether status notifications are enabled for the Connector. Default is `true`.
        /// </summary>
        [Input("statusUpdatesEnabled")]
        public Input<bool>? StatusUpdatesEnabled { get; set; }

        public TwingateConnectorState()
        {
        }
        public static new TwingateConnectorState Empty => new TwingateConnectorState();
    }
}
