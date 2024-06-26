// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Emailbob.Twingate.Inputs
{

    public sealed class TwingateResourceProtocolsGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Whether to allow ICMP (ping) traffic
        /// </summary>
        [Input("allowIcmp")]
        public Input<bool>? AllowIcmp { get; set; }

        [Input("tcp")]
        public Input<Inputs.TwingateResourceProtocolsTcpGetArgs>? Tcp { get; set; }

        [Input("udp")]
        public Input<Inputs.TwingateResourceProtocolsUdpGetArgs>? Udp { get; set; }

        public TwingateResourceProtocolsGetArgs()
        {
        }
        public static new TwingateResourceProtocolsGetArgs Empty => new TwingateResourceProtocolsGetArgs();
    }
}
